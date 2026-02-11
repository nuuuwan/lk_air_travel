import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from typing import Optional

import httpx

from flights.Airport import Airport

SCHEDULE_URL = "https://www.airport.lk/flight_info/flightdetails_load"
DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
SL_TZ = timezone(timedelta(hours=5, minutes=30))
DAY_INDEX = {d: i for i, d in enumerate(DAYS)}

# Single airports with city/airport format (not multi-leg flights)
SINGLE_AIRPORT_CITIES = {
    "London/Heathrow",
    "Chengdu/Tianfu",
}


def _parse_airport_name(raw_name: str) -> str:
    """Parse airport name to handle multi-leg flights and city/airport format.

    For single airports with city/airport format (e.g., London/Heathrow),
    replace "/" with "-" to avoid confusion.

    For multi-leg flights (e.g., Dubai/Male), extract the second airport
    as the actual origin since the flight stops there en route to Colombo.
    """
    if "/" not in raw_name:
        return raw_name

    # Check if this is a known single airport with city/airport format
    if raw_name in SINGLE_AIRPORT_CITIES:
        return raw_name.replace("/", "-")

    # Otherwise, it's a multi-leg flight - use the second airport
    parts = raw_name.split("/")
    return parts[-1].strip()


def _to_unix_time(day: str, hhmm: str) -> int:
    """Convert a day-of-week + HHMM string to a Unix timestamp.

    Uses the current week's date in Sri Lanka time (UTC+5:30).
    """
    now = datetime.now(SL_TZ)
    monday = now - timedelta(days=now.weekday())
    monday = monday.replace(hour=0, minute=0, second=0, microsecond=0)
    target = monday + timedelta(days=DAY_INDEX[day])
    hour = int(hhmm[:2])
    minute = int(hhmm[2:])
    target = target.replace(hour=hour, minute=minute)
    return int(target.timestamp())


@dataclass
class Flight:
    id: str
    airline: str
    flight_no: str
    aircraft_type: str
    ut_arrival_time: int
    airport_name: str
    country_name: str
    airport_latlng: Optional[tuple[float, float]]
    notes: str

    @property
    def file_path(self) -> str:
        """Generate filename: <flight_num>_<YYYYMMDD>_<HHMM>.json"""
        dt = datetime.fromtimestamp(self.ut_arrival_time, SL_TZ)
        date_str = dt.strftime("%Y%m%d")
        time_str = dt.strftime("%H%M")
        return f"{self.flight_no}_{date_str}_{time_str}.json"

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Flight":
        return cls(**data)

    def to_json_file(self, path: str):
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def from_json_file(cls, path: str) -> "Flight":
        with open(path, "r") as f:
            return cls.from_dict(json.load(f))

    @classmethod
    def fetch_and_store_cmb_arrivals(cls, data_dir: str) -> list["Flight"]:
        """Fetch inbound flights to CMB and save to disk.

        Saves each flight as an individual JSON file under
        data_dir/flights/ and an aggregated data_dir/flights.json.

        Returns the list of Flight objects.
        """
        flights_dir = os.path.join(data_dir, "flights")
        os.makedirs(flights_dir, exist_ok=True)

        all_flights = []
        for day in DAYS:
            response = httpx.post(
                SCHEDULE_URL,
                data={
                    "arr_day": day,
                    "flghtType": "0",
                    "isAjax": "true",
                },
            )
            response.raise_for_status()
            for raw in response.json():
                raw_airport_name = raw["from_via"].strip()
                airport_name = _parse_airport_name(raw_airport_name)
                airport = Airport.from_name(airport_name)
                flight = cls(
                    id=raw["id"],
                    airline=raw["airline"].strip(),
                    flight_no=raw["flight_no"].strip(),
                    aircraft_type=raw["aircraft_type"].strip(),
                    ut_arrival_time=_to_unix_time(
                        day,
                        raw["est_arrival_time"].strip(),
                    ),
                    airport_name=airport_name,
                    country_name=(
                        airport.country_name if airport else "Unknown"
                    ),
                    airport_latlng=airport.latlng if airport else None,
                    notes=raw["notes"].strip(),
                )
                all_flights.append(flight)
                flight.to_json_file(
                    os.path.join(flights_dir, flight.file_path)
                )

        agg_path = os.path.join(data_dir, "flights.json")
        with open(agg_path, "w") as f:
            json.dump(
                [fl.to_dict() for fl in all_flights],
                f,
                indent=2,
            )

        return all_flights

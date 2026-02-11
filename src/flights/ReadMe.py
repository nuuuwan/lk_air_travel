import json
import os
from collections import Counter
from datetime import datetime, timedelta, timezone


class ReadMe:
    """Summarizes flights.json and updates README.md."""

    def __init__(self, data_dir: str, readme_path: str):
        self.data_dir = data_dir
        self.readme_path = readme_path
        flights_json = os.path.join(data_dir, "flights.json")
        with open(flights_json, "r") as f:
            self.flights = json.load(f)

    def _get_airline_table(self, airline_counts: Counter) -> list[str]:
        lines = [
            "## Airlines",
            "",
            "| Airline | Flights |",
            "|---------|---------------|",
        ]
        for airline, count in airline_counts.most_common():
            lines.append(f"| {airline} | {count} |")
        return lines

    @staticmethod
    def _get_country_flag(country: str) -> str:
        """Get flag emoji for a country."""
        flag_map = {
            "United Arab Emirates": "🇦🇪",
            "India": "🇮🇳",
            "Qatar": "🇶🇦",
            "Malaysia": "🇲🇾",
            "Maldives": "🇲🇻",
            "Singapore": "🇸🇬",
            "Thailand": "🇹🇭",
            "Kuwait": "🇰🇼",
            "Bangladesh": "🇧🇩",
            "Turkey": "🇹🇷",
            "United Kingdom": "🇬🇧",
            "Saudi Arabia": "🇸🇦",
            "Indonesia": "🇮🇩",
            "China": "🇨🇳",
            "Australia": "🇦🇺",
            "Hong Kong": "🇭🇰",
            "Oman": "🇴🇲",
            "Pakistan": "🇵🇰",
            "Nepal": "🇳🇵",
            "Japan": "🇯🇵",
            "France": "🇫🇷",
            "Germany": "🇩🇪",
            "Russia": "🇷🇺",
            "Seychelles": "🇸🇨",
            "Poland": "🇵🇱",
            "Kazakhstan": "🇰🇿",
            "South Korea": "🇰🇷",
            "Switzerland": "🇨🇭",
            "Bahrain/Maldives": "🇧🇭",
            "United Arab Emirates/Maldives": "🇦🇪",
            "Turkey/India": "🇹🇷",
            "Poland/UAE": "🇵🇱",
        }
        return flag_map.get(country, "🏳️")

    def _get_country_table(self, country_counts: Counter) -> list[str]:
        lines = [
            "## Countries",
            "",
            "| Country | Flights |",
            "|---------|---------------|",
        ]
        for country, count in country_counts.most_common():
            flag = self._get_country_flag(country)
            lines.append(f"| {flag} {country} | {count} |")
        return lines

    def _get_origin_table(
        self, origin_counts: Counter, airport_to_country: dict
    ) -> list[str]:
        lines = [
            "## Inbound Locations",
            "",
            "| Country | Origin | Flights |",
            "|---------|--------|---------------|",
        ]
        for origin, count in origin_counts.most_common():
            country = airport_to_country.get(origin, "Unknown")
            flag = self._get_country_flag(country)
            lines.append(f"| {flag} {country} | {origin} | {count} |")
        return lines

    def _summary_md(self) -> str:
        origins = sorted(
            {f["airport_name"] for f in self.flights if f["airport_name"]}
        )
        airlines = sorted({f["airline"] for f in self.flights if f["airline"]})
        countries = sorted(
            {f["country_name"] for f in self.flights if f["country_name"]}
        )
        airline_counts = Counter(f["airline"] for f in self.flights)
        country_counts = Counter(
            f["country_name"] for f in self.flights if f["country_name"]
        )
        origin_counts = Counter(
            f["airport_name"] for f in self.flights if f["airport_name"]
        )

        # Create mapping of airport to country
        airport_to_country = {
            f["airport_name"]: f["country_name"]
            for f in self.flights
            if f["airport_name"]
        }

        # Get current timestamp for last updated badge
        sl_tz = timezone(timedelta(hours=5, minutes=30))
        now = datetime.now(sl_tz)
        timestamp = now.strftime("%Y--%m--%d_%H:%M:%S")

        # Calculate time window for all flights
        if self.flights:
            min_time = min(f["ut_arrival_time"] for f in self.flights)
            max_time = max(f["ut_arrival_time"] for f in self.flights)
            start_date = datetime.fromtimestamp(min_time, sl_tz)
            end_date = datetime.fromtimestamp(max_time, sl_tz)
            date_range = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
        else:
            date_range = "N/A"

        # Get latest flight for example
        latest_flight = max(self.flights, key=lambda f: f["ut_arrival_time"])
        example_dt = datetime.fromtimestamp(
            latest_flight["ut_arrival_time"], sl_tz
        )
        example_date = example_dt.strftime("%Y-%m-%d %H:%M")

        lines = [
            "# Air Travel in 🇱🇰 Sri Lanka (lk_air_travel)",
            "",
            f"![LastUpdated](https://img.shields.io/badge/last_updated-{timestamp}-green)",
            "",
            "![Flight Map](images/flight_map.png)",
            "",
            "## Introduction",
            "",
            "This repository provides automated tracking of inbound flight "
            "schedules to Colombo's Bandaranaike International Airport (CMB). "
            "Flight data is fetched from the official airport website and "
            "updated daily via GitHub Actions.",
            "",
            "**Data Source:** <https://www.airport.lk>",
            "",
            "**Note on Multi-Leg Flights:** For flights that make intermediate "
            "stops before arriving in Colombo (e.g., a flight from Dubai stopping "
            "in Male), the origin airport is recorded as the last stop before "
            "Colombo (Male), not the initial departure point (Dubai). This reflects "
            "the actual boarding location for the final leg to Colombo.",
            "",
            "Each flight record includes:",
            "- Flight number and airline",
            "- Aircraft type",
            "- Arrival time (Sri Lanka timezone)",
            "- Origin airport with country and coordinates",
            "",
            "### Example Flight Data",
            "",
            "```json",
            "{",
            f'  "flight_no": "{latest_flight["flight_no"]}",',
            f'  "airline": "{latest_flight["airline"]}",',
            f'  "aircraft_type": "{latest_flight["aircraft_type"]}",',
            f'  "arrival_time": "{example_date}",',
            f'  "airport_name": "{latest_flight["airport_name"]}",',
            f'  "country_name": "{latest_flight["country_name"]}"',
            "}",
            "```",
            "",
            "## Summary Statistics",
            "",
            f"**Scheduled flights for the week: {date_range}**",
            "",
            f"- **{len(self.flights)}** total flights",
            f"- **{len(origins)}** origins",
            f"- **{len(countries)}** countries",
            f"- **{len(airlines)}** airlines",
            "",
        ]
        lines += self._get_airline_table(airline_counts)
        lines.append("")
        lines += self._get_country_table(country_counts)
        lines.append("")
        lines += self._get_origin_table(origin_counts, airport_to_country)
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append(
            "![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)"
        )
        lines.append(
            "![MadeWith](https://img.shields.io/badge/made_with-python-blue)"
        )
        lines.append(
            "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]"
            "(https://opensource.org/licenses/MIT)"
        )
        lines.append("")
        return "\n".join(lines)

    def write(self):
        md = self._summary_md()
        with open(self.readme_path, "w") as f:
            f.write(md)

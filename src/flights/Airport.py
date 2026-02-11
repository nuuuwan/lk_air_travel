"""Airport metadata including country names and coordinates."""

import json
import os
from dataclasses import dataclass
from functools import cache, lru_cache


@dataclass
class Airport:
    name: str
    country_name: str
    latlng: tuple[float, float]

    @classmethod
    @lru_cache(maxsize=1)
    def _load_airports_data(cls) -> dict[str, dict]:
        """Load airports data from JSON file."""
        data_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "data", "airports.json"
        )
        with open(data_path, "r") as f:
            return json.load(f)

    @classmethod
    def from_dict(cls, data: dict) -> "Airport":
        """Create Airport from dictionary."""
        return cls(
            name=data["name"],
            country_name=data["country_name"],
            latlng=tuple(data["latlng"]),
        )

    @classmethod
    @cache
    def list_all(cls) -> list["Airport"]:
        """Return all airports."""
        data = cls._load_airports_data()
        return [cls.from_dict(airport_data) for airport_data in data.values()]

    @classmethod
    @cache
    def from_name(cls, name: str) -> "Airport | None":
        airports = cls.list_all()
        idx = {airport.name: airport for airport in airports}
        return idx.get(name)

import json
import os
from collections import Counter


class ReadMe:
    """Summarizes flights.json and updates README.md."""

    def __init__(self, data_dir: str, readme_path: str):
        self.data_dir = data_dir
        self.readme_path = readme_path
        flights_json = os.path.join(data_dir, "flights.json")
        with open(flights_json, "r") as f:
            self.flights = json.load(f)

    def _summary_md(self) -> str:
        origins = sorted(
            {f["airport_name"] for f in self.flights if f["airport_name"]}
        )
        airlines = sorted({f["airline"] for f in self.flights if f["airline"]})
        airline_counts = Counter(f["airline"] for f in self.flights)
        origin_counts = Counter(
            f["airport_name"] for f in self.flights if f["airport_name"]
        )

        lines = [
            "# lk_air_travel",
            "",
            "Inbound flight schedule to Colombo (CMB)"
            " - Bandaranaike International Airport.",
            "",
            f"- **{len(self.flights)}** weekly flights",
            f"- **{len(origins)}** origins",
            f"- **{len(airlines)}** airlines",
            "",
            "## Airlines",
            "",
            "| Airline | Weekly Flights |",
            "|---------|---------------|",
        ]
        for airline, count in airline_counts.most_common():
            lines.append(f"| {airline} | {count} |")

        lines += [
            "",
            "## Inbound Locations",
            "",
            "| Origin | Weekly Flights |",
            "|--------|---------------|",
        ]
        for origin, count in origin_counts.most_common():
            lines.append(f"| {origin} | {count} |")

        lines.append("")
        return "\n".join(lines)

    def write(self):
        md = self._summary_md()
        with open(self.readme_path, "w") as f:
            f.write(md)

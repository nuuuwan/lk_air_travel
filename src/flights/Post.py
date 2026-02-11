import json
import os
from collections import Counter
from datetime import datetime, timedelta, timezone


class Post:
    """Generates POST.txt with a Twitter/X thread in plain text format."""

    POST_PATH = "POST.txt"

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        flights_json = os.path.join(data_dir, "flights.json")
        with open(flights_json, "r") as f:
            self.flights = json.load(f)

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

    def _get_airline_list(
        self, airline_counts: Counter, top_n: int = 10
    ) -> str:
        """Generate plain text list for top airlines."""
        lines = []
        for idx, (airline, count) in enumerate(
            airline_counts.most_common(top_n), 1
        ):
            lines.append(f"{idx}. {airline}: {count} flights/week")
        return "\n".join(lines)

    def _get_country_list(
        self,
        country_counts: Counter,
        country_to_airports: dict,
        top_n: int = 10,
    ) -> str:
        """Generate plain text list for top countries."""
        lines = []
        for idx, (country, count) in enumerate(
            country_counts.most_common(top_n), 1
        ):
            flag = self._get_country_flag(country)
            destinations = len(country_to_airports.get(country, []))
            lines.append(
                f"{idx}. {flag} {country}: {count} flights ({destinations} destinations)"
            )
        return "\n".join(lines)

    def _get_origin_list(
        self,
        origin_counts: Counter,
        airport_to_country: dict,
        top_n: int = 10,
    ) -> str:
        """Generate plain text list for top origins."""
        lines = []
        for idx, (origin, count) in enumerate(
            origin_counts.most_common(top_n), 1
        ):
            country = airport_to_country.get(origin, "Unknown")
            flag = self._get_country_flag(country)
            lines.append(f"{idx}. {flag} {origin}: {count} flights/week")
        return "\n".join(lines)

    def _generate_thread(self) -> str:
        """Generate the Twitter/X thread content."""
        origins = sorted(
            {f["airport_name"] for f in self.flights if f["airport_name"]}
        )
        airlines = sorted(
            {f["airline"] for f in self.flights if f["airline"]}
        )
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

        # Create mapping of country to airports (for destinations count)
        country_to_airports = {}
        for f in self.flights:
            if f.get("country_name") and f.get("airport_name"):
                country = f["country_name"]
                airport = f["airport_name"]
                if country not in country_to_airports:
                    country_to_airports[country] = set()
                country_to_airports[country].add(airport)

        # Calculate time window for all flights
        if self.flights:
            sl_tz = timezone(timedelta(hours=5, minutes=30))
            min_time = min(f["ut_arrival_time"] for f in self.flights)
            max_time = max(f["ut_arrival_time"] for f in self.flights)
            start_date = datetime.fromtimestamp(min_time, sl_tz)
            end_date = datetime.fromtimestamp(max_time, sl_tz)
            date_range = f"{
                start_date.strftime('%Y-%m-%d')} to {
                end_date.strftime('%Y-%m-%d')}"
        else:
            date_range = "N/A"

        # Thread content
        lines = []

        # Tweet 1: Introduction
        lines.append("1/ Air Travel Data for Sri Lanka 🇱🇰")
        lines.append("")
        lines.append(
            f"Tracking inbound flights to Colombo (CMB) for {date_range}"
        )
        lines.append("")
        lines.append(f"• {len(self.flights)} total flights")
        lines.append(f"• {len(countries)} countries")
        lines.append(f"• {len(origins)} origin airports")
        lines.append(f"• {len(airlines)} airlines")
        lines.append("")
        lines.append(
            "Sri Lanka's aviation landscape reveals patterns about its economy, tourism, diaspora connections, and strategic location on global routes."
        )
        lines.append("")
        lines.append("#SriLanka #Aviation #Data #CMB")
        lines.append("")
        lines.append(
            "Flight Map: https://github.com/nuuuwan/lk_air_travel/blob/main/images/flight_map.png"
        )
        lines.append("Data Source: https://www.airport.lk")
        lines.append("GitHub: https://github.com/nuuuwan/lk_air_travel")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 2: Airlines
        lines.append("2/ Top Airlines by Weekly Flights")
        lines.append("")
        lines.append(self._get_airline_list(airline_counts, top_n=10))
        lines.append("")
        lines.append("#Airlines #AviationIndustry")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 3: Countries
        lines.append("3/ Top Countries by Connectivity")
        lines.append("")
        lines.append(
            self._get_country_list(
                country_counts, country_to_airports, top_n=10
            )
        )
        lines.append("")
        lines.append("#GlobalConnectivity #IndianOcean")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 4: Origins
        lines.append("4/ Top Inbound Locations")
        lines.append("")
        lines.append(
            self._get_origin_list(origin_counts, airport_to_country, top_n=10)
        )
        lines.append("")
        lines.append("#TravelRoutes #AirportData")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tweet 5: Disclaimer
        lines.append("5/ About This Dataset")
        lines.append("")
        lines.append(
            "This is a living dataset - automatically updated daily via GitHub Actions. Data is scraped from the official CMB airport website, providing real-time insights into Sri Lanka's aviation connectivity."
        )
        lines.append("")
        lines.append(
            "Future plans: historical trend analysis, seasonal patterns, airline market share evolution, route launch/cancellation tracking."
        )
        lines.append("")
        lines.append(
            "Feedback and contributions welcome! Interested in outbound flights, cargo data, or other aviation analytics? Let me know."
        )
        lines.append("")
        lines.append(
            "Report issues: https://github.com/nuuuwan/lk_air_travel/issues"
        )
        lines.append("Contribute: https://github.com/nuuuwan/lk_air_travel")
        lines.append("")
        lines.append("#OpenData #GitHub #DataScience")
        lines.append("")

        return "\n".join(lines)

    def write(self):
        """Write the POST.txt file."""
        content = self._generate_thread()
        with open(self.POST_PATH, "w") as f:
            f.write(content)

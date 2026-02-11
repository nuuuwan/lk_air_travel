"""Generate a world map showing flight routes to Colombo."""

import json
import os
from datetime import datetime, timedelta, timezone

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt


class FlightMap:
    """Creates a map visualization of flights to Colombo."""

    CMB_COORDS = (6.8218, 79.8850)  # Colombo coordinates
    MAP_PATH = os.path.join("images", "flight_map.png")

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        flights_json = os.path.join(data_dir, "flights.json")
        with open(flights_json, "r") as f:
            self.flights = json.load(f)

    def _get_unique_airports(self) -> list[tuple[str, float, float, int]]:
        """Get unique airports with their coordinates and flight counts."""
        airport_counts = {}
        for flight in self.flights:
            airport = flight["airport_name"]
            latlng = flight.get("airport_latlng")
            if latlng and airport not in airport_counts:
                airport_counts[airport] = {
                    "latlng": latlng,
                    "count": 0,
                }
            if airport in airport_counts:
                airport_counts[airport]["count"] += 1

        return [
            (name, data["latlng"][0], data["latlng"][1], data["count"])
            for name, data in airport_counts.items()
        ]

    def create_map(self):
        """Create and save the flight map."""
        airports = self._get_unique_airports()

        # Calculate unique countries
        unique_countries = set(
            flight.get("country_name")
            for flight in self.flights
            if flight.get("country_name")
        )
        num_countries = len(unique_countries)

        # Create figure with PlateCarree projection
        fig = plt.figure(figsize=(20, 12), facecolor="white")
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_facecolor("white")

        # Add map features
        ax.add_feature(cfeature.LAND, facecolor="#f0f0f0", edgecolor="none")
        ax.add_feature(cfeature.OCEAN, facecolor="#e3f2fd")

        # Highlight countries with available flights
        shpfilename = shpreader.natural_earth(
            resolution="110m", category="cultural", name="admin_0_countries"
        )
        reader = shpreader.Reader(shpfilename)
        countries = reader.records()

        # Country name mapping for better matching
        country_name_map = {
            "United Arab Emirates": "UAE",
            "United States of America": "USA",
            "United Kingdom": "UK",
            "Russian Federation": "Russia",
            "Republic of Korea": "South Korea",
            "Peoples Republic of China": "China",
            "Republic of Serbia": "Serbia",
        }

        for country in countries:
            country_name = country.attributes.get(
                "NAME_LONG"
            ) or country.attributes.get("NAME")
            # Check if this country has flights (with mapping)
            mapped_name = country_name_map.get(country_name, country_name)
            if (
                country_name in unique_countries
                or mapped_name in unique_countries
            ):
                ax.add_geometries(
                    [country.geometry],
                    ccrs.PlateCarree(),
                    facecolor="#a5d6a7",
                    edgecolor="none",
                    alpha=0.6,
                    zorder=1,
                )

        ax.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor="#666666")
        ax.add_feature(
            cfeature.BORDERS, linewidth=0.3, edgecolor="#999999", alpha=0.5
        )

        # Calculate bounding box for all airports (including CMB)
        all_lons = [lon for _, _, lon, _ in airports] + [self.CMB_COORDS[1]]
        all_lats = [lat for _, lat, _, _ in airports] + [self.CMB_COORDS[0]]

        min_lon, max_lon = min(all_lons), max(all_lons)
        min_lat, max_lat = min(all_lats), max(all_lats)

        # Add padding (15% on each side)
        lon_range = max_lon - min_lon
        lat_range = max_lat - min_lat
        padding_lon = lon_range * 0.15
        padding_lat = lat_range * 0.15

        # Set extent to bounding box with padding
        ax.set_extent(
            [
                min_lon - padding_lon,
                max_lon + padding_lon,
                min_lat - padding_lat,
                max_lat + padding_lat,
            ],
            crs=ccrs.PlateCarree(),
        )

        # Draw routes
        for airport_name, lat, lon, count in airports:
            # Draw line from airport to Colombo (great circle)
            # Scale line thickness and opacity based on flight volume
            alpha = min(0.25 + (count / 70) * 0.65, 0.9)
            linewidth = min(0.5 + (count / 15), 5.5)

            ax.plot(
                [lon, self.CMB_COORDS[1]],
                [lat, self.CMB_COORDS[0]],
                color="#1565c0",
                alpha=alpha,
                linewidth=linewidth,
                transform=ccrs.Geodetic(),
                zorder=2,
            )

            # Draw origin airport marker - area proportional to flight volume
            # In matplotlib scatter, 's' parameter is area in points^2
            size = count * 8  # Area directly proportional to flight count
            ax.scatter(
                lon,
                lat,
                s=size,
                color="#ff6b35",
                alpha=0.8,
                edgecolors="#d32f2f",
                linewidths=1.5,
                transform=ccrs.PlateCarree(),
                zorder=3,
            )

        # Add title and labels
        ax.text(
            0.5,
            0.97,
            "Inbound Flight Routes to Colombo (CMB)",
            transform=ax.transAxes,
            fontsize=24,
            fontweight="bold",
            color="#1a237e",
            ha="center",
            va="top",
        )

        # Calculate date range
        sl_tz = timezone(timedelta(hours=5, minutes=30))
        if self.flights:
            min_time = min(f["ut_arrival_time"] for f in self.flights)
            max_time = max(f["ut_arrival_time"] for f in self.flights)
            start_date = datetime.fromtimestamp(min_time, sl_tz)
            end_date = datetime.fromtimestamp(max_time, sl_tz)
            date_range = f"{
                start_date.strftime('%b %d')} - {
                end_date.strftime('%b %d, %Y')}"
        else:
            date_range = "N/A"

        ax.text(
            0.5,
            0.93,
            f"{len(self.flights)} flights from {len(airports)} airports in {num_countries} countries ({date_range})",
            transform=ax.transAxes,
            fontsize=14,
            color="#424242",
            ha="center",
            va="top",
        )

        # Add gridlines
        gl = ax.gridlines(
            draw_labels=False,
            linewidth=0.5,
            color="#cccccc",
            alpha=0.5,
            linestyle="--",
        )

        # Save the figure
        os.makedirs(os.path.dirname(self.MAP_PATH), exist_ok=True)
        plt.tight_layout()
        plt.savefig(
            self.MAP_PATH, dpi=150, facecolor="white", bbox_inches="tight"
        )
        plt.close()

        print(f"Flight map saved to {self.MAP_PATH}")

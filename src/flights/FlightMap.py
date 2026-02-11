"""Generate a world map showing flight routes to Colombo."""

import json
import os

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt


class FlightMap:
    """Creates a map visualization of flights to Colombo."""

    CMB_COORDS = (6.8218, 79.8850)  # Colombo coordinates

    def __init__(self, data_dir: str, output_path: str):
        self.data_dir = data_dir
        self.output_path = output_path
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

        # Set global extent
        ax.set_global()

        # Draw routes
        for airport_name, lat, lon, count in airports:
            # Draw line from airport to Colombo (great circle)
            alpha = min(0.2 + (count / 100) * 0.6, 0.7)
            linewidth = min(0.8 + (count / 40), 3.0)

            ax.plot(
                [lon, self.CMB_COORDS[1]],
                [lat, self.CMB_COORDS[0]],
                color="#1565c0",
                alpha=alpha,
                linewidth=linewidth,
                transform=ccrs.Geodetic(),
                zorder=2,
            )

            # Draw origin airport marker
            size = min(30 + (count / 8), 150)
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

        # Draw Colombo marker (circle with distinct color)
        ax.scatter(
            self.CMB_COORDS[1],
            self.CMB_COORDS[0],
            s=size,
            color="#7b1fa2",
            marker="o",
            edgecolors="#4a148c",
            linewidths=2.5,
            transform=ccrs.PlateCarree(),
            zorder=4,
            label="Colombo (CMB)",
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

        ax.text(
            0.5,
            0.93,
            f"{len(self.flights)} weekly flights from {len(airports)} airports in {num_countries} countries",
            transform=ax.transAxes,
            fontsize=14,
            color="#424242",
            ha="center",
            va="top",
        )

        # Add legend
        ax.legend(
            loc="lower right",
            fontsize=12,
            facecolor="white",
            edgecolor="#666666",
            framealpha=0.9,
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
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        plt.tight_layout()
        plt.savefig(
            self.output_path, dpi=150, facecolor="white", bbox_inches="tight"
        )
        plt.close()

        print(f"Flight map saved to {self.output_path}")

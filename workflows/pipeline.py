import os

from flights import Flight, FlightMap
from flights.ReadMe import ReadMe

DIR = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(DIR, "data")
README_PATH = os.path.join(DIR, "README.md")
MAP_PATH = os.path.join(DIR, "images", "flight_map.png")


def get_cmb_inbound_locations():
    """Fetch inbound flights to CMB, store as JSON, print origins."""
    print("Fetching inbound flight schedule to CMB (Bandaranaike Intl)...\n")

    all_flights = Flight.fetch_and_store_cmb_arrivals(DATA_DIR)
    all_origins = {f.airport_name for f in all_flights if f.airport_name}

    print(f"Stored {len(all_flights)} flights to data/flights/")
    print("Aggregated to data/flights.json")

    FlightMap(DATA_DIR, MAP_PATH).create_map()
    print("Generated flight map")

    ReadMe(DATA_DIR, README_PATH).write()
    print("Updated README.md")

    print(f"\nFound {len(all_origins)} unique inbound locations:\n")
    for origin in sorted(all_origins):
        print(f"- {origin}")

    return sorted(all_origins)


if __name__ == "__main__":
    get_cmb_inbound_locations()

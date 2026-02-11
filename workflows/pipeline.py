import os

from flights import Flight

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def get_cmb_inbound_locations():
    """Fetch inbound flights to CMB, store as JSON, print origins."""
    print("Fetching inbound flight schedule to CMB (Bandaranaike Intl)...\n")

    all_flights = Flight.fetch_and_store_cmb_arrivals(DATA_DIR)
    all_origins = {f.from_via for f in all_flights if f.from_via}

    print(f"Stored {len(all_flights)} flights to data/flights/")
    print("Aggregated to data/flights.json")
    print(f"\nFound {len(all_origins)} unique inbound locations:\n")
    for origin in sorted(all_origins):
        print(f"- {origin}")

    return sorted(all_origins)


if __name__ == "__main__":
    get_cmb_inbound_locations()

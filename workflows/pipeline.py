from flights import Flight, FlightMap
from flights.Post import Post
from flights.ReadMe import ReadMe


def main():
    Flight.fetch_and_store_cmb_arrivals()
    FlightMap().create_map()
    ReadMe().write()
    Post().write()


if __name__ == "__main__":
    main()

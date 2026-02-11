"""Airport metadata including country names and coordinates."""

from typing import Optional

# Airport database with country and lat/lng information
# Format: airport_name -> (country_name, (latitude, longitude))
AIRPORT_DATA = {
    "Abu Dhabi": ("United Arab Emirates", (24.4330, 54.6511)),
    "Almaty International Airport": ("Kazakhstan", (43.3521, 77.0405)),
    "Bahrain/Male": (
        "Bahrain/Maldives",
        (26.2708, 50.6336),
    ),  # Multi-leg flight
    "Bangalore": ("India", (13.1986, 77.7066)),
    "Bangkok Don Mueang": ("Thailand", (13.9126, 100.6074)),
    "Bangkok Suvarnabhumi": ("Thailand", (13.6900, 100.7501)),
    "Chengdu/Tianfu": ("China", (30.3089, 104.4419)),
    "Chennai": ("India", (12.9902, 80.1693)),
    "Chongqing": ("China", (29.7193, 106.6419)),
    "Cochin": ("India", (10.1520, 76.3874)),
    "Dammam": ("Saudi Arabia", (26.4715, 49.7979)),
    "Delhi": ("India", (28.5562, 77.1000)),
    "Dhaka": ("Bangladesh", (23.8434, 90.3978)),
    "Doha": ("Qatar", (25.2731, 51.6080)),
    "Dubai": ("United Arab Emirates", (25.2532, 55.3657)),
    "Dubai/Male": (
        "United Arab Emirates/Maldives",
        (25.2532, 55.3657),
    ),  # Multi-leg
    "Frankfurt Main": ("Germany", (50.0379, 8.5622)),
    "Gan Intl": ("Maldives", (-0.6942, 73.1556)),
    "Gdansk Im Lecha Walesy/Ras Al Khaimah Intl": (
        "Poland/UAE",
        (54.3776, 18.4662),
    ),
    "Guangzhou Baiyun": ("China", (23.3924, 113.2988)),
    "Hong Kong": ("Hong Kong", (22.3080, 113.9185)),
    "Hyderabad Intl": ("India", (17.2403, 78.4294)),
    "Incheon": ("South Korea", (37.4602, 126.4407)),
    "Istanbul Ataturk": ("Turkey", (40.9769, 28.8146)),
    "Istanbul Ataturk/Chennai": (
        "Turkey/India",
        (40.9769, 28.8146),
    ),  # Multi-leg
    "Jakarta": ("Indonesia", (-6.1256, 106.6559)),
    "Karachi": ("Pakistan", (24.9065, 67.1608)),
    "Kathmandu": ("Nepal", (27.6966, 85.3591)),
    "Katowice Intl/Ras Al Khaimah Intl": ("Poland/UAE", (50.4743, 19.0800)),
    "Kuala Lumpur": ("Malaysia", (2.7456, 101.7098)),
    "Kunming": ("China", (25.1019, 102.9292)),
    "Kuwait": ("Kuwait", (29.2266, 47.9689)),
    "Lahore": ("Pakistan", (31.5216, 74.4036)),
    "London/Heathrow": ("United Kingdom", (51.4700, -0.4543)),
    "Madurai": ("India", (9.8345, 78.0934)),
    "Male": ("Maldives", (4.1917, 73.5290)),
    "Melbourne": ("Australia", (-37.6690, 144.8410)),
    "Mumbai": ("India", (19.0896, 72.8656)),
    "Muscat": ("Oman", (23.5933, 58.2844)),
    "Narita": ("Japan", (35.7720, 140.3929)),
    "Paris Charles de Gaulle": ("France", (49.0097, 2.5479)),
    "Poznan/Ras Al Khaimah Intl": ("Poland/UAE", (52.4215, 16.8263)),
    "Riyadh": ("Saudi Arabia", (24.9577, 46.6989)),
    "Seychelles": ("Seychelles", (-4.6740, 55.5218)),
    "Shanghai": ("China", (31.1443, 121.8083)),
    "Sharjah": ("United Arab Emirates", (25.3286, 55.5172)),
    "Sheremetyevo": ("Russia", (55.9726, 37.4146)),
    "Singapore": ("Singapore", (1.3644, 103.9915)),
    "Sydney": ("Australia", (-33.9461, 151.1772)),
    "Thiruvananthapuram": ("India", (8.4821, 76.9200)),
    "Tiruchirappalli": ("India", (10.7654, 78.7097)),
    "Warsaw Chopin Intl/Ras Al Khaimah Intl": (
        "Poland/UAE",
        (52.1657, 20.9671),
    ),
    "Zurich Intl": ("Switzerland", (47.4647, 8.5492)),
}


def get_airport_country(airport_name: str) -> str:
    """Get country name for an airport."""
    data = AIRPORT_DATA.get(airport_name)
    if data:
        return data[0]
    return "Unknown"


def get_airport_latlng(airport_name: str) -> Optional[tuple[float, float]]:
    """Get latitude and longitude for an airport."""
    data = AIRPORT_DATA.get(airport_name)
    if data:
        return data[1]
    return None

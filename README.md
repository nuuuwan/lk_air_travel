# Air Travel in 🇱🇰 Sri Lanka (lk_air_travel)

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_13:45:34-green)

![Flight Map](images/flight_map.png)

## Introduction

This repository provides automated tracking of inbound flight schedules to Colombo's Bandaranaike International Airport (CMB). Flight data is fetched from the official airport website and updated daily via GitHub Actions.

**Data Source:** <https://www.airport.lk>

**Note on Multi-Leg Flights:** For flights that make intermediate stops before arriving in Colombo (e.g., a flight from Dubai stopping in Male), the origin airport is recorded as the last stop before Colombo (Male), not the initial departure point (Dubai). This reflects the actual boarding location for the final leg to Colombo.

Each flight record includes:
- Flight number and airline
- Aircraft type
- Arrival time (Sri Lanka timezone)
- Origin airport with country and coordinates

### Example Flight Data

```json
{
  "flight_no": "TG307",
  "airline": "Thai Airways",
  "aircraft_type": "A320",
  "arrival_time": "2026-09-06 23:55",
  "airport_name": "Bangkok",
  "country_name": "Unknown"
}
```

## Summary Statistics

**Scheduled flights for the week: 2026-08-31 to 2026-09-06**

- **621** total flights
- **44** origins
- **22** countries
- **28** airlines

## Airlines

| # | Airline | Flights/Week |
|---:|---------|-------------:|
| 1 | Srilankan Airlines | 252 |
| 2 | Indigo Airlines | 47 |
| 3 | Qatar Airways | 35 |
| 4 | Fly Dubai | 28 |
| 5 | Emirates | 28 |
| 6 | Etihad Airways | 27 |
| 7 | Fits Air | 26 |
| 8 | Air India | 21 |
| 9 | Air Arabia | 20 |
| 10 | Singapore Airlines | 14 |
| 11 | Jazeera Airways | 11 |
| 12 | Turkish Airlines | 11 |
| 13 | China Eastern | 11 |
| 14 | Malaysia Airlines | 10 |
| 15 | Batik Air | 9 |
| 16 | Kuwait Airways | 7 |
| 17 | Salam Air | 7 |
| 18 | Gulf Air | 7 |
| 19 | Air China | 7 |
| 20 | Air Asia Berhad | 7 |
| 21 | Cathay Pacific | 7 |
| 22 | Thai Airways | 7 |
| 23 | Chongqing Airlines | 6 |
| 24 | Air Arabia Abu Dhabi | 5 |
| 25 | Jetstar Airways | 3 |
| 26 | Viet Jet | 3 |
| 27 | Vietnam Airlines | 3 |
| 28 | Air Seychelles | 2 |

## Countries

| # | Country | Destinations | Flights/Week |
|---:|---------|-------------:|-------------:|
| 1 | 🇮🇳 India | 7 | 146 |
| 2 | 🇦🇪 United Arab Emirates | 3 | 108 |
| 3 | 🏳️ Unknown | 9 | 67 |
| 4 | 🇲🇻 Maldives | 2 | 58 |
| 5 | 🇶🇦 Qatar | 1 | 42 |
| 6 | 🇲🇾 Malaysia | 1 | 35 |
| 7 | 🇸🇬 Singapore | 1 | 28 |
| 8 | 🇰🇼 Kuwait | 1 | 24 |
| 9 | 🇨🇳 China | 4 | 18 |
| 10 | 🇸🇦 Saudi Arabia | 2 | 14 |
| 11 | 🇧🇩 Bangladesh | 1 | 12 |
| 12 | 🇹🇷 Turkey | 1 | 11 |
| 13 | 🇦🇺 Australia | 1 | 10 |
| 14 | 🇵🇰 Pakistan | 2 | 8 |
| 15 | 🇴🇲 Oman | 1 | 7 |
| 16 | 🇬🇧 United Kingdom | 1 | 7 |
| 17 | 🇮🇩 Indonesia | 1 | 7 |
| 18 | 🇭🇰 Hong Kong | 1 | 7 |
| 19 | 🇳🇵 Nepal | 1 | 4 |
| 20 | 🇯🇵 Japan | 1 | 4 |
| 21 | 🇸🇨 Seychelles | 1 | 2 |
| 22 | 🇰🇷 South Korea | 1 | 2 |

## Inbound Locations

| # | Country | Origin | Flights/Week |
|---:|---------|--------|-------------:|
| 1 | 🇦🇪 United Arab Emirates | Dubai | 56 |
| 2 | 🇲🇻 Maldives | Male | 56 |
| 3 | 🇮🇳 India | Chennai | 48 |
| 4 | 🇶🇦 Qatar | Doha | 42 |
| 5 | 🇲🇾 Malaysia | Kuala Lumpur | 35 |
| 6 | 🇦🇪 United Arab Emirates | Abu Dhabi | 32 |
| 7 | 🇮🇳 India | Delhi | 28 |
| 8 | 🇮🇳 India | Mumbai | 28 |
| 9 | 🇸🇬 Singapore | Singapore | 28 |
| 10 | 🏳️ Unknown | Bangkok | 26 |
| 11 | 🇰🇼 Kuwait | Kuwait | 24 |
| 12 | 🇦🇪 United Arab Emirates | Sharjah | 20 |
| 13 | 🇮🇳 India | Bangalore | 17 |
| 14 | 🇧🇩 Bangladesh | Dhaka | 12 |
| 15 | 🇹🇷 Turkey | Istanbul Ataturk | 11 |
| 16 | 🇮🇳 India | Hyderabad Intl | 11 |
| 17 | 🇦🇺 Australia | Melbourne | 10 |
| 18 | 🏳️ Unknown | Tiruchchirapalli | 8 |
| 19 | 🇴🇲 Oman | Muscat | 7 |
| 20 | 🇸🇦 Saudi Arabia | Dammam | 7 |
| 21 | 🇸🇦 Saudi Arabia | Riyadh | 7 |
| 22 | 🇬🇧 United Kingdom | London-Heathrow | 7 |
| 23 | 🇮🇳 India | Madurai | 7 |
| 24 | 🇮🇳 India | Cochin | 7 |
| 25 | 🇮🇩 Indonesia | Jakarta | 7 |
| 26 | 🇨🇳 China | Shanghai | 7 |
| 27 | 🏳️ Unknown | Chengdu Tianfu | 7 |
| 28 | 🇭🇰 Hong Kong | Hong Kong | 7 |
| 29 | 🏳️ Unknown | Frankfurt Airport | 6 |
| 30 | 🏳️ Unknown | Ho Chi Minh Intl | 6 |
| 31 | 🇵🇰 Pakistan | Karachi | 4 |
| 32 | 🏳️ Unknown | Trivandrum | 4 |
| 33 | 🇵🇰 Pakistan | Lahore | 4 |
| 34 | 🇳🇵 Nepal | Kathmandu | 4 |
| 35 | 🇨🇳 China | Kunming | 4 |
| 36 | 🇨🇳 China | Guangzhou Baiyun | 4 |
| 37 | 🇯🇵 Japan | Narita | 4 |
| 38 | 🏳️ Unknown | Sydney Airport | 4 |
| 39 | 🏳️ Unknown | Paris Charles de Gaulle Airport | 3 |
| 40 | 🏳️ Unknown | Ahmedabad Intl | 3 |
| 41 | 🇨🇳 China | Chongqing | 3 |
| 42 | 🇸🇨 Seychelles | Seychelles | 2 |
| 43 | 🇰🇷 South Korea | Incheon | 2 |
| 44 | 🇲🇻 Maldives | Gan Intl | 2 |

---

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Air Travel in 🇱🇰 Sri Lanka (lk_air_travel)

![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_01:22:57-green)

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
  "flight_no": "MU713",
  "airline": "China Eastern",
  "aircraft_type": "A332",
  "arrival_time": "2026-03-01 23:40",
  "airport_name": "Kunming",
  "country_name": "China"
}
```

## Summary Statistics

**Scheduled flights for the week: 2026-02-23 to 2026-03-01**

- **644** total flights
- **47** origins
- **27** countries
- **29** airlines

## Airlines

| # | Airline | Flights/Week |
|---:|---------|-------------:|
| 1 | Srilankan Airlines | 258 |
| 2 | Indigo Airlines | 54 |
| 3 | Qatar Airways | 35 |
| 4 | Fly Dubai | 33 |
| 5 | Emirates | 28 |
| 6 | Etihad Airways | 27 |
| 7 | Fits Air | 26 |
| 8 | Air India | 21 |
| 9 | Air Arabia | 20 |
| 10 | Air Asia Berhad | 14 |
| 11 | China Eastern | 14 |
| 12 | Turkish Airlines | 11 |
| 13 | THAI AIR ASIA | 10 |
| 14 | Singapore Airlines | 10 |
| 15 | Gulf Air | 9 |
| 16 | Malaysia Airlines | 9 |
| 17 | Enter Air | 8 |
| 18 | Thai Airways | 7 |
| 19 | Jazeera Airways | 7 |
| 20 | Air China | 7 |
| 21 | Cathay Pacific | 7 |
| 22 | Chongqing Airlines | 6 |
| 23 | Salam Air | 5 |
| 24 | Air Arabia Abu Dhabi | 5 |
| 25 | Kuwait Airways | 4 |
| 26 | Aeroflot | 3 |
| 27 | Air Seychelles | 2 |
| 28 | Air Astana | 2 |
| 29 | Edelweiss Air | 2 |

## Countries

| # | Country | Destinations | Flights/Week |
|---:|---------|-------------:|-------------:|
| 1 | 🇮🇳 India | 9 | 167 |
| 2 | 🇦🇪 United Arab Emirates | 4 | 125 |
| 3 | 🇲🇻 Maldives | 2 | 57 |
| 4 | 🇶🇦 Qatar | 1 | 42 |
| 5 | 🇲🇾 Malaysia | 1 | 40 |
| 6 | 🇹🇭 Thailand | 2 | 33 |
| 7 | 🇨🇳 China | 5 | 28 |
| 8 | 🇸🇬 Singapore | 1 | 24 |
| 9 | 🇰🇼 Kuwait | 1 | 18 |
| 10 | 🇧🇩 Bangladesh | 1 | 14 |
| 11 | 🇸🇦 Saudi Arabia | 2 | 14 |
| 12 | 🇦🇺 Australia | 2 | 11 |
| 13 | 🇹🇷 Turkey | 1 | 10 |
| 14 | 🇬🇧 United Kingdom | 1 | 9 |
| 15 | 🇵🇰 Pakistan | 2 | 8 |
| 16 | 🇮🇩 Indonesia | 1 | 7 |
| 17 | 🇭🇰 Hong Kong | 1 | 7 |
| 18 | 🇴🇲 Oman | 1 | 5 |
| 19 | 🇳🇵 Nepal | 1 | 4 |
| 20 | 🇯🇵 Japan | 1 | 4 |
| 21 | 🇫🇷 France | 1 | 3 |
| 22 | 🇩🇪 Germany | 1 | 3 |
| 23 | 🇷🇺 Russia | 1 | 3 |
| 24 | 🇸🇨 Seychelles | 1 | 2 |
| 25 | 🇰🇿 Kazakhstan | 1 | 2 |
| 26 | 🇰🇷 South Korea | 1 | 2 |
| 27 | 🇨🇭 Switzerland | 1 | 2 |

## Inbound Locations

| # | Country | Origin | Flights/Week |
|---:|---------|--------|-------------:|
| 1 | 🇦🇪 United Arab Emirates | Dubai | 65 |
| 2 | 🇲🇻 Maldives | Male | 55 |
| 3 | 🇮🇳 India | Chennai | 50 |
| 4 | 🇶🇦 Qatar | Doha | 42 |
| 5 | 🇲🇾 Malaysia | Kuala Lumpur | 40 |
| 6 | 🇦🇪 United Arab Emirates | Abu Dhabi | 32 |
| 7 | 🇮🇳 India | Mumbai | 28 |
| 8 | 🇮🇳 India | Delhi | 28 |
| 9 | 🇸🇬 Singapore | Singapore | 24 |
| 10 | 🇮🇳 India | Bangalore | 24 |
| 11 | 🇹🇭 Thailand | Bangkok Suvarnabhumi | 23 |
| 12 | 🇦🇪 United Arab Emirates | Sharjah | 20 |
| 13 | 🇰🇼 Kuwait | Kuwait | 18 |
| 14 | 🇧🇩 Bangladesh | Dhaka | 14 |
| 15 | 🇮🇳 India | Hyderabad Intl | 12 |
| 16 | 🇹🇷 Turkey | Istanbul Ataturk | 10 |
| 17 | 🇹🇭 Thailand | Bangkok Don Mueang | 10 |
| 18 | 🇬🇧 United Kingdom | London-Heathrow | 9 |
| 19 | 🇦🇪 United Arab Emirates | Ras Al Khaimah Intl | 8 |
| 20 | 🇮🇳 India | Tiruchirappalli | 8 |
| 21 | 🇸🇦 Saudi Arabia | Dammam | 7 |
| 22 | 🇸🇦 Saudi Arabia | Riyadh | 7 |
| 23 | 🇮🇩 Indonesia | Jakarta | 7 |
| 24 | 🇮🇳 India | Cochin | 7 |
| 25 | 🇨🇳 China | Shanghai | 7 |
| 26 | 🇨🇳 China | Chengdu-Tianfu | 7 |
| 27 | 🇦🇺 Australia | Melbourne | 7 |
| 28 | 🇭🇰 Hong Kong | Hong Kong | 7 |
| 29 | 🇨🇳 China | Kunming | 7 |
| 30 | 🇮🇳 India | Madurai | 6 |
| 31 | 🇴🇲 Oman | Muscat | 5 |
| 32 | 🇵🇰 Pakistan | Karachi | 4 |
| 33 | 🇮🇳 India | Thiruvananthapuram | 4 |
| 34 | 🇳🇵 Nepal | Kathmandu | 4 |
| 35 | 🇵🇰 Pakistan | Lahore | 4 |
| 36 | 🇨🇳 China | Guangzhou Baiyun | 4 |
| 37 | 🇯🇵 Japan | Narita | 4 |
| 38 | 🇦🇺 Australia | Sydney | 4 |
| 39 | 🇫🇷 France | Paris Charles de Gaulle | 3 |
| 40 | 🇩🇪 Germany | Frankfurt Main | 3 |
| 41 | 🇨🇳 China | Chongqing | 3 |
| 42 | 🇷🇺 Russia | Sheremetyevo | 3 |
| 43 | 🇸🇨 Seychelles | Seychelles | 2 |
| 44 | 🇰🇿 Kazakhstan | Almaty International Airport | 2 |
| 45 | 🇰🇷 South Korea | Incheon | 2 |
| 46 | 🇨🇭 Switzerland | Zurich Intl | 2 |
| 47 | 🇲🇻 Maldives | Gan Intl | 2 |

---

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

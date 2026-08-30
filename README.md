# Air Travel in 🇱🇰 Sri Lanka (lk_air_travel)

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_09:42:37-green)

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
  "arrival_time": "2026-08-30 23:55",
  "airport_name": "Bangkok Suvarnabhumi",
  "country_name": "Thailand"
}
```

## Summary Statistics

**Scheduled flights for the week: 2026-08-24 to 2026-08-30**

- **601** total flights
- **44** origins
- **25** countries
- **27** airlines

## Airlines

| # | Airline | Flights/Week |
|---:|---------|-------------:|
| 1 | Srilankan Airlines | 249 |
| 2 | Indigo Airlines | 40 |
| 3 | Qatar Airways | 35 |
| 4 | Fly Dubai | 28 |
| 5 | Emirates | 28 |
| 6 | Etihad Airways | 27 |
| 7 | Fits Air | 24 |
| 8 | Air Arabia | 20 |
| 9 | Air India | 18 |
| 10 | Jazeera Airways | 14 |
| 11 | Singapore Airlines | 14 |
| 12 | Turkish Airlines | 11 |
| 13 | China Eastern | 11 |
| 14 | Malaysia Airlines | 10 |
| 15 | Kuwait Airways | 7 |
| 16 | Gulf Air | 7 |
| 17 | Air Asia Berhad | 7 |
| 18 | THAI AIR ASIA | 7 |
| 19 | Cathay Pacific | 7 |
| 20 | Thai Airways | 7 |
| 21 | Salam Air | 6 |
| 22 | Chongqing Airlines | 6 |
| 23 | Air Arabia Abu Dhabi | 5 |
| 24 | Air China | 4 |
| 25 | Air Seychelles | 3 |
| 26 | Batik Air | 3 |
| 27 | Viet Jet | 3 |

## Countries

| # | Country | Destinations | Flights/Week |
|---:|---------|-------------:|-------------:|
| 1 | 🇮🇳 India | 8 | 140 |
| 2 | 🇦🇪 United Arab Emirates | 3 | 107 |
| 3 | 🇲🇻 Maldives | 2 | 56 |
| 4 | 🇶🇦 Qatar | 1 | 42 |
| 5 | 🇲🇾 Malaysia | 1 | 34 |
| 6 | 🇹🇭 Thailand | 2 | 28 |
| 7 | 🇸🇬 Singapore | 1 | 28 |
| 8 | 🇰🇼 Kuwait | 1 | 27 |
| 9 | 🇨🇳 China | 5 | 22 |
| 10 | 🇸🇦 Saudi Arabia | 2 | 14 |
| 11 | 🇧🇩 Bangladesh | 1 | 13 |
| 12 | 🇹🇷 Turkey | 1 | 11 |
| 13 | 🏳️ Unknown | 2 | 11 |
| 14 | 🇦🇺 Australia | 2 | 11 |
| 15 | 🇵🇰 Pakistan | 2 | 8 |
| 16 | 🇬🇧 United Kingdom | 1 | 7 |
| 17 | 🇮🇩 Indonesia | 1 | 7 |
| 18 | 🇭🇰 Hong Kong | 1 | 7 |
| 19 | 🇴🇲 Oman | 1 | 6 |
| 20 | 🇸🇨 Seychelles | 1 | 6 |
| 21 | 🇳🇵 Nepal | 1 | 4 |
| 22 | 🇯🇵 Japan | 1 | 4 |
| 23 | 🇫🇷 France | 1 | 3 |
| 24 | 🇩🇪 Germany | 1 | 3 |
| 25 | 🇰🇷 South Korea | 1 | 2 |

## Inbound Locations

| # | Country | Origin | Flights/Week |
|---:|---------|--------|-------------:|
| 1 | 🇦🇪 United Arab Emirates | Dubai | 55 |
| 2 | 🇲🇻 Maldives | Male | 54 |
| 3 | 🇶🇦 Qatar | Doha | 42 |
| 4 | 🇮🇳 India | Chennai | 41 |
| 5 | 🇲🇾 Malaysia | Kuala Lumpur | 34 |
| 6 | 🇦🇪 United Arab Emirates | Abu Dhabi | 32 |
| 7 | 🇮🇳 India | Delhi | 28 |
| 8 | 🇸🇬 Singapore | Singapore | 28 |
| 9 | 🇰🇼 Kuwait | Kuwait | 27 |
| 10 | 🇮🇳 India | Mumbai | 26 |
| 11 | 🇹🇭 Thailand | Bangkok Suvarnabhumi | 21 |
| 12 | 🇦🇪 United Arab Emirates | Sharjah | 20 |
| 13 | 🇮🇳 India | Bangalore | 17 |
| 14 | 🇧🇩 Bangladesh | Dhaka | 13 |
| 15 | 🇹🇷 Turkey | Istanbul Ataturk | 11 |
| 16 | 🇮🇳 India | Hyderabad Intl | 10 |
| 17 | 🏳️ Unknown | Ho Chi Minh Intl | 8 |
| 18 | 🇸🇦 Saudi Arabia | Dammam | 7 |
| 19 | 🇸🇦 Saudi Arabia | Riyadh | 7 |
| 20 | 🇬🇧 United Kingdom | London-Heathrow | 7 |
| 21 | 🇮🇳 India | Madurai | 7 |
| 22 | 🇮🇳 India | Cochin | 7 |
| 23 | 🇮🇩 Indonesia | Jakarta | 7 |
| 24 | 🇨🇳 China | Shanghai | 7 |
| 25 | 🇹🇭 Thailand | Bangkok Don Mueang | 7 |
| 26 | 🇦🇺 Australia | Melbourne | 7 |
| 27 | 🇭🇰 Hong Kong | Hong Kong | 7 |
| 28 | 🇴🇲 Oman | Muscat | 6 |
| 29 | 🇸🇨 Seychelles | Seychelles | 6 |
| 30 | 🇵🇰 Pakistan | Karachi | 4 |
| 31 | 🇮🇳 India | Thiruvananthapuram | 4 |
| 32 | 🇵🇰 Pakistan | Lahore | 4 |
| 33 | 🇳🇵 Nepal | Kathmandu | 4 |
| 34 | 🇨🇳 China | Chengdu-Tianfu | 4 |
| 35 | 🇨🇳 China | Kunming | 4 |
| 36 | 🇨🇳 China | Guangzhou Baiyun | 4 |
| 37 | 🇯🇵 Japan | Narita | 4 |
| 38 | 🇦🇺 Australia | Sydney | 4 |
| 39 | 🇫🇷 France | Paris Charles de Gaulle | 3 |
| 40 | 🇩🇪 Germany | Frankfurt Main | 3 |
| 41 | 🏳️ Unknown | Ahmedabad Intl | 3 |
| 42 | 🇨🇳 China | Chongqing | 3 |
| 43 | 🇰🇷 South Korea | Incheon | 2 |
| 44 | 🇲🇻 Maldives | Gan Intl | 2 |

---

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

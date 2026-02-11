# Air Travel in 🇱🇰 Sri Lanka (lk_air_travel)

![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_18:45:55-green)

![Flight Map](images/flight_map.png)

## Introduction

This repository provides automated tracking of inbound flight schedules to Colombo's Bandaranaike International Airport (CMB). Flight data is fetched from the official airport website and updated daily via GitHub Actions.

**Data Source:** <https://www.airport.lk>

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
  "arrival_time": "2026-02-15 23:40",
  "airport_name": "Kunming",
  "country_name": "China"
}
```

## Summary Statistics

**Scheduled flights for the week: 2026-02-09 to 2026-02-15**

- **644** total flights
- **53** origins
- **31** countries
- **29** airlines

## Airlines

| Airline | Flights |
|---------|---------------|
| Srilankan Airlines | 258 |
| Indigo Airlines | 54 |
| Qatar Airways | 35 |
| Fly Dubai | 33 |
| Emirates | 28 |
| Etihad Airways | 27 |
| Fits Air | 26 |
| Air India | 21 |
| Air Arabia | 20 |
| Air Asia Berhad | 14 |
| China Eastern | 14 |
| Turkish Airlines | 11 |
| THAI AIR ASIA | 10 |
| Singapore Airlines | 10 |
| Gulf Air | 9 |
| Malaysia Airlines | 9 |
| Enter Air | 8 |
| Thai Airways | 7 |
| Jazeera Airways | 7 |
| Air China | 7 |
| Cathay Pacific | 7 |
| Chongqing Airlines | 6 |
| Salam Air | 5 |
| Air Arabia Abu Dhabi | 5 |
| Kuwait Airways | 4 |
| Aeroflot | 3 |
| Air Seychelles | 2 |
| Air Astana | 2 |
| Edelweiss Air | 2 |

## Countries

| Country | Flights |
|---------|---------------|
| 🇮🇳 India | 166 |
| 🇦🇪 United Arab Emirates | 117 |
| 🇶🇦 Qatar | 42 |
| 🇲🇾 Malaysia | 40 |
| 🇲🇻 Maldives | 34 |
| 🇹🇭 Thailand | 33 |
| 🇨🇳 China | 28 |
| 🇸🇬 Singapore | 24 |
| 🇰🇼 Kuwait | 18 |
| 🇧🇩 Bangladesh | 14 |
| 🇸🇦 Saudi Arabia | 14 |
| 🇦🇪 United Arab Emirates/Maldives | 14 |
| 🇦🇺 Australia | 11 |
| 🇹🇷 Turkey | 10 |
| 🇬🇧 United Kingdom | 9 |
| 🇧🇭 Bahrain/Maldives | 9 |
| 🇵🇱 Poland/UAE | 8 |
| 🇵🇰 Pakistan | 8 |
| 🇮🇩 Indonesia | 7 |
| 🇭🇰 Hong Kong | 7 |
| 🇴🇲 Oman | 5 |
| 🇳🇵 Nepal | 4 |
| 🇯🇵 Japan | 4 |
| 🇫🇷 France | 3 |
| 🇩🇪 Germany | 3 |
| 🇷🇺 Russia | 3 |
| 🇸🇨 Seychelles | 2 |
| 🇰🇿 Kazakhstan | 2 |
| 🇰🇷 South Korea | 2 |
| 🇨🇭 Switzerland | 2 |
| 🇹🇷 Turkey/India | 1 |

## Inbound Locations

| Country | Origin | Flights |
|---------|--------|---------------|
| 🇦🇪 United Arab Emirates | Dubai | 65 |
| 🇮🇳 India | Chennai | 49 |
| 🇶🇦 Qatar | Doha | 42 |
| 🇲🇾 Malaysia | Kuala Lumpur | 40 |
| 🇦🇪 United Arab Emirates | Abu Dhabi | 32 |
| 🇲🇻 Maldives | Male | 32 |
| 🇮🇳 India | Mumbai | 28 |
| 🇮🇳 India | Delhi | 28 |
| 🇸🇬 Singapore | Singapore | 24 |
| 🇮🇳 India | Bangalore | 24 |
| 🇹🇭 Thailand | Bangkok Suvarnabhumi | 23 |
| 🇦🇪 United Arab Emirates | Sharjah | 20 |
| 🇰🇼 Kuwait | Kuwait | 18 |
| 🇧🇩 Bangladesh | Dhaka | 14 |
| 🇦🇪 United Arab Emirates/Maldives | Dubai/Male | 14 |
| 🇮🇳 India | Hyderabad Intl | 12 |
| 🇹🇷 Turkey | Istanbul Ataturk | 10 |
| 🇹🇭 Thailand | Bangkok Don Mueang | 10 |
| 🇬🇧 United Kingdom | London/Heathrow | 9 |
| 🇧🇭 Bahrain/Maldives | Bahrain/Male | 9 |
| 🇮🇳 India | Tiruchirappalli | 8 |
| 🇸🇦 Saudi Arabia | Dammam | 7 |
| 🇸🇦 Saudi Arabia | Riyadh | 7 |
| 🇮🇩 Indonesia | Jakarta | 7 |
| 🇮🇳 India | Cochin | 7 |
| 🇨🇳 China | Shanghai | 7 |
| 🇨🇳 China | Chengdu/Tianfu | 7 |
| 🇦🇺 Australia | Melbourne | 7 |
| 🇭🇰 Hong Kong | Hong Kong | 7 |
| 🇨🇳 China | Kunming | 7 |
| 🇮🇳 India | Madurai | 6 |
| 🇴🇲 Oman | Muscat | 5 |
| 🇵🇰 Pakistan | Karachi | 4 |
| 🇮🇳 India | Thiruvananthapuram | 4 |
| 🇳🇵 Nepal | Kathmandu | 4 |
| 🇵🇰 Pakistan | Lahore | 4 |
| 🇨🇳 China | Guangzhou Baiyun | 4 |
| 🇯🇵 Japan | Narita | 4 |
| 🇦🇺 Australia | Sydney | 4 |
| 🇫🇷 France | Paris Charles de Gaulle | 3 |
| 🇩🇪 Germany | Frankfurt Main | 3 |
| 🇨🇳 China | Chongqing | 3 |
| 🇷🇺 Russia | Sheremetyevo | 3 |
| 🇸🇨 Seychelles | Seychelles | 2 |
| 🇵🇱 Poland/UAE | Katowice Intl/Ras Al Khaimah Intl | 2 |
| 🇵🇱 Poland/UAE | Poznan/Ras Al Khaimah Intl | 2 |
| 🇵🇱 Poland/UAE | Gdansk Im Lecha Walesy/Ras Al Khaimah Intl | 2 |
| 🇵🇱 Poland/UAE | Warsaw Chopin Intl/Ras Al Khaimah Intl | 2 |
| 🇰🇿 Kazakhstan | Almaty International Airport | 2 |
| 🇰🇷 South Korea | Incheon | 2 |
| 🇨🇭 Switzerland | Zurich Intl | 2 |
| 🇲🇻 Maldives | Gan Intl | 2 |
| 🇹🇷 Turkey/India | Istanbul Ataturk/Chennai | 1 |

---

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

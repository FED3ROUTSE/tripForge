CITY_TO_COUNTRY = {
    "paris": "france",
    "bucharest": "romania",
    "rome": "italy",
    "london": "united kingdom",
    "new york": "united states",
    "sydney": "australia",
    "dubai": "united arab emirates",
    "tokyo": "japan",
    "san francisco": "united states",
    "rio de janeiro": "brazil",
    "athens": "greece",
    "beijing": "china",
    "berlin": "germany",
    "cairo": "egypt",
    "istanbul": "turkey",
    "lisbon": "portugal",
    "moscow": "russia",
    "new delhi": "india",
    "prague": "czech republic",
    "seoul": "south korea",
    "shanghai": "china",
    "singapore": "singapore",
    "st. petersburg": "russia",
    "washington d.c.": "united states",
    "vienna": "austria",
    "amsterdam": "netherlands",
    "madrid": "spain",
    "budapest": "hungary",
    "hanoi": "vietnam",
    "mexico city": "mexico",
    "toronto": "canada",
    "los angeles": "united states",
    "dublin": "ireland",
    "kuala lumpur": "malaysia",
    "bangkok": "thailand",
}

COUNTRY_TO_CURRENCY = {
    "france": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "romania": {"code": "RON", "symbol": "lei", "name": "Romanian Leu"},
    "italy": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "united kingdom": {"code": "GBP", "symbol": "£", "name": "Pound Sterling"},
    "united states": {"code": "USD", "symbol": "$", "name": "US Dollar"},
    "australia": {"code": "AUD", "symbol": "$", "name": "Australian Dollar"},
    "united arab emirates": {"code": "AED", "symbol": "د.إ", "name": "UAE Dirham"},
    "japan": {"code": "JPY", "symbol": "¥", "name": "Yen"},
    "brazil": {"code": "BRL", "symbol": "R$", "name": "Brazilian Real"},
    "greece": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "china": {"code": "CNY", "symbol": "¥", "name": "Yuan"},
    "germany": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "egypt": {"code": "EGP", "symbol": "£", "name": "Egyptian Pound"},
    "turkey": {"code": "TRY", "symbol": "₺", "name": "Turkish Lira"},
    "portugal": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "russia": {"code": "RUB", "symbol": "₽", "name": "Russian Ruble"},
    "india": {"code": "INR", "symbol": "₹", "name": "Indian Rupee"},
    "czech republic": {"code": "CZK", "symbol": "Kč", "name": "Czech Koruna"},
    "south korea": {"code": "KRW", "symbol": "₩", "name": "Won"},
    "singapore": {"code": "SGD", "symbol": "$", "name": "Singapore Dollar"},
    "austria": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "netherlands": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "spain": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "hungary": {"code": "HUF", "symbol": "Ft", "name": "Hungarian Forint"},
    "vietnam": {"code": "VND", "symbol": "₫", "name": "Vietnamese Dong"},
    "mexico": {"code": "MXN", "symbol": "$", "name": "Mexican Peso"},
    "canada": {"code": "CAD", "symbol": "$", "name": "Canadian Dollar"},
    "ireland": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "malaysia": {"code": "MYR", "symbol": "RM", "name": "Malaysian Ringgit"},
    "thailand": {"code": "THB", "symbol": "฿", "name": "Thai Baht"},
}


COUNTRY_TO_PEAK_SEASON = {
    "france": [(6, 8)],                      # June–August
    "romania": [(6, 8)],                     # June–August
    "italy": [(6, 8)],                       # June–August
    "united kingdom": [(6, 8)],              # June–August
    "united states": [(6, 8)],               # June–August
    "australia": [(12, 2)],                  # December–February
    "united arab emirates": [(11, 3)],       # November–March
    "japan": [(3, 4), (10, 11)],             # Cherry blossom + autumn
    "brazil": [(12, 2)],                     # December–February
    "greece": [(6, 8)],                      # June–August
    "china": [(4, 5), (9, 10)],              # Spring + Golden Week
    "germany": [(6, 9)],                     # June–September
    "egypt": [(10, 3)],                      # October–March
    "turkey": [(6, 8)],                      # June–August
    "portugal": [(6, 8)],                    # June–August
    "russia": [(6, 8)],                      # June–August
    "india": [(11, 2)],                      # November–February
    "czech republic": [(6, 9)],               # June–September
    "south korea": [(4, 6), (9, 10)],         # Spring + autumn
    "singapore": [(6, 8)],                   # Summer holidays
    "austria": [(6, 9)],                     # June–September
    "netherlands": [(4, 9)],                 # Tulips + summer
    "spain": [(6, 8)],                       # June–August
    "hungary": [(6, 9)],                     # June–September
    "vietnam": [(12, 4)],                    # Dry season
    "mexico": [(12, 4)],                     # Dry season
    "canada": [(6, 9)],                      # June–September
    "ireland": [(6, 8)],                     # June–August
    "malaysia": [(12, 2)],                   # Dry season
    "thailand": [(11, 2)],                   # Cool & dry
}

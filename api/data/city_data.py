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
    "krakow": "poland"
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
    "poland": {"code": "PLN", "symbol": "zł", "name": "Polish Zloty"},

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
    "poland": [(5, 9)],   # May–September

}

COUNTRY_TO_POPULAR_ATTRACTIONS = {
    "france": ["Eiffel Tower", "Louvre Museum", "Mont Saint-Michel"],
    "romania": ["Bran Castle", "Transfăgărășan Highway", "Sibiu Old Town"],
    "italy": ["Colosseum", "Vatican City", "Venice Canals"],
    "united kingdom": ["Big Ben", "Tower of London", "Stonehenge"],
    "united states": ["Statue of Liberty", "Grand Canyon", "Times Square"],
    "australia": ["Sydney Opera House", "Great Barrier Reef", "Bondi Beach"],
    "united arab emirates": ["Burj Khalifa", "Palm Jumeirah", "Dubai Mall"],
    "japan": ["Mount Fuji", "Kyoto Temples", "Tokyo Skytree"],
    "brazil": ["Christ the Redeemer", "Sugarloaf Mountain", "Copacabana Beach"],
    "greece": ["Acropolis", "Parthenon", "Delphi"],
    "china": ["Great Wall", "Forbidden City", "Terracotta Army"],
    "germany": ["Brandenburg Gate", "Neuschwanstein Castle", "Cologne Cathedral"],
    "egypt": ["Pyramids of Giza", "Valley of the Kings", "Karnak Temple"],
    "turkey": ["Hagia Sophia", "Cappadocia", "Blue Mosque"],
    "portugal": ["Belém Tower", "Jerónimos Monastery", "Algarve Coast"],
    "russia": ["Red Square", "Saint Basil’s Cathedral", "Hermitage Museum"],
    "india": ["Taj Mahal", "Jaipur City Palace", "Varanasi Ghats"],
    "czech republic": ["Charles Bridge", "Prague Castle", "Old Town Square"],
    "south korea": ["Gyeongbokgung Palace", "Bukchon Hanok Village", "Jeju Island"],
    "singapore": ["Marina Bay Sands", "Gardens by the Bay", "Sentosa Island"],
    "austria": ["Schönbrunn Palace", "Hallstatt", "Vienna State Opera"],
    "netherlands": ["Anne Frank House", "Keukenhof Gardens", "Canals of Amsterdam"],
    "spain": ["Sagrada Família", "Alhambra", "Park Güell"],
    "hungary": ["Buda Castle", "Parliament Building", "Thermal Baths"],
    "vietnam": ["Ha Long Bay", "Hoi An Old Town", "Cu Chi Tunnels"],
    "mexico": ["Chichén Itzá", "Tulum", "Mexico City Historic Center"],
    "canada": ["Niagara Falls", "Banff National Park", "CN Tower"],
    "ireland": ["Cliffs of Moher", "Dublin Castle", "Ring of Kerry"],
    "malaysia": ["Petronas Towers", "Batu Caves", "Langkawi"],
    "thailand": ["Grand Palace", "Phi Phi Islands", "Wat Arun"],
    "poland": [
    "Wawel Castle",
    "Auschwitz-Birkenau Memorial",
    "Old Town Square (Krakow)"
],

}


COUNTRY_TO_LOCAL_CUISINE = {
    "france": ["Croissant", "Boeuf Bourguignon", "Crème Brûlée"],
    "romania": ["Sarmale", "Mămăligă", "Ciorbă"],
    "italy": ["Pizza", "Pasta", "Risotto"],
    "united kingdom": ["Fish and Chips", "Full English Breakfast", "Sunday Roast"],
    "united states": ["Burgers", "BBQ Ribs", "Apple Pie"],
    "australia": ["Meat Pie", "Vegemite", "Barramundi"],
    "united arab emirates": ["Machboos", "Shawarma", "Luqaimat"],
    "japan": ["Sushi", "Ramen", "Tempura"],
    "brazil": ["Feijoada", "Pão de Queijo", "Churrasco"],
    "greece": ["Moussaka", "Souvlaki", "Tzatziki"],
    "china": ["Peking Duck", "Dumplings", "Kung Pao Chicken"],
    "germany": ["Bratwurst", "Sauerbraten", "Pretzels"],
    "egypt": ["Koshari", "Ful Medames", "Molokhia"],
    "turkey": ["Kebab", "Baklava", "Meze"],
    "portugal": ["Bacalhau", "Pastel de Nata", "Caldo Verde"],
    "russia": ["Borscht", "Pelmeni", "Blini"],
    "india": ["Butter Chicken", "Biryani", "Naan"],
    "czech republic": ["Svíčková", "Goulash", "Trdelník"],
    "south korea": ["Kimchi", "Bibimbap", "Bulgogi"],
    "singapore": ["Hainanese Chicken Rice", "Chili Crab", "Laksa"],
    "austria": ["Wiener Schnitzel", "Apple Strudel", "Sachertorte"],
    "netherlands": ["Stroopwafels", "Haring", "Bitterballen"],
    "spain": ["Paella", "Tapas", "Churros"],
    "hungary": ["Goulash", "Lángos", "Paprikash"],
    "vietnam": ["Pho", "Banh Mi", "Spring Rolls"],
    "mexico": ["Tacos", "Enchiladas", "Guacamole"],
    "canada": ["Poutine", "Maple Syrup", "Butter Tarts"],
    "ireland": ["Irish Stew", "Soda Bread", "Boxty"],
    "malaysia": ["Nasi Lemak", "Satay", "Rendang"],
    "thailand": ["Pad Thai", "Green Curry", "Tom Yum Soup"],
    "poland": [
    "Pierogi",
    "Bigos",
    "Żurek"
],

}

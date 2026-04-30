# =======================
# CITY → COUNTRY
# =======================

LANDMARK = {
    "paris": "Eiffel Tower",
    "bucharest": "the Palace of Parliament of Bucharest",
    "rome": "Colosseum of rome best picture",
    "london": "Big ben best picture",
    "new york": "Statue of Liberty best view",
    "sydney": "Sydney Opera House best view",
    "dubai": "Burj Khalifa best view",
    "tokyo": "Tokyo Skytree best view",
    "san francisco": "Golden Gate Bridge best view",
    "rio de janeiro": "Christ the Redeemer best view",
    "athens": "Acropolis of Athens best view",
    "beijing": "Forbidden City best view",
    "berlin": "A high-resolution, ultra-sharp daytime photograph of the Brandenburg Gate in Berlin. Clear blue sky, natural sunlight, wide-angle view from the front, people walking around, realistic colors and detailed architecture.",
    "cairo": "Pyramids of Giza best view",
    "istanbul": "A high-resolution, ultra-sharp nighttime panoramic photograph of the Hagia Sophia Grand Mosque in Istanbul, beautifully illuminated with warm golden lights. Wide angle view, clear sky, vibrant reflections, dramatic contrast, professional architectural photography.",
    "lisbon": "Belém Tower best view",
    "moscow": "Saint Basil's Cathedral of Moscow, best picture",
    "new delhi": "India Gate in new delhi best picture",
    "prague": "Charles Bridge best view",
    "seoul": "Gyeongbokgung Palace best view",
    "shanghai": "The Bund best view",
    "singapore": "Marina Bay Sands best view",
    "st. petersburg": "The Hermitage Museum best view",
    "washington d.c.": "United States Capitol Building best view",
    "vienna": "Schönbrunn Palace best view",
    "amsterdam": "Rijksmuseum best view",
    "madrid": "Plaza Mayor, Madrid best view",
    "budapest": "Hungarian Parliament Building best view",
    "hanoi": "Hanoi Opera House best view",
    "mexico city": "Ángel de la Independencia best view",
    "toronto": "CN Tower best view",
    "los angeles": "Hollywood Sign best view",
    "dublin": "Ha'penny Bridge best view",
    "kuala lumpur": "Petronas Twin Towers best view",
    "bangkok": "Wat Arun best view",
}


CITY_TO_COUNTRY = {
    # Original
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
    "krakow": "poland",

    # Added Europe
    "barcelona": "spain",
    "milan": "italy",
    "florence": "italy",
    "venice": "italy",
    "naples": "italy",
    "munich": "germany",
    "zurich": "switzerland",
    "geneva": "switzerland",
    "brussels": "belgium",
    "edinburgh": "united kingdom",
    "manchester": "united kingdom",
    "reykjavik": "iceland",
    "stockholm": "sweden",
    "oslo": "norway",
    "copenhagen": "denmark",
    "helsinki": "finland",

    # Americas
    "miami": "united states",
    "las vegas": "united states",
    "chicago": "united states",
    "boston": "united states",
    "san diego": "united states",
    "vancouver": "canada",
    "montreal": "canada",
    "quebec city": "canada",
    "buenos aires": "argentina",
    "lima": "peru",

    # Asia
    "hong kong": "hong kong",
    "taipei": "taiwan",
    "osaka": "japan",
    "kyoto": "japan",
    "phuket": "thailand",
    "chiang mai": "thailand",
    "bali": "indonesia",
    "jakarta": "indonesia",
    "manila": "philippines",
    "ho chi minh city": "vietnam",

    # Middle East & Africa
    "doha": "qatar",
    "riyadh": "saudi arabia",
    "marrakech": "morocco",
    "casablanca": "morocco",
    "cape town": "south africa",
    "johannesburg": "south africa",

    # Oceania
    "melbourne": "australia",
    "auckland": "new zealand",
    "queenstown": "new zealand",
}


# =======================
# COUNTRY → CURRENCY
# =======================

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

    # Added
    "switzerland": {"code": "CHF", "symbol": "CHF", "name": "Swiss Franc"},
    "belgium": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "iceland": {"code": "ISK", "symbol": "kr", "name": "Icelandic Króna"},
    "sweden": {"code": "SEK", "symbol": "kr", "name": "Swedish Krona"},
    "norway": {"code": "NOK", "symbol": "kr", "name": "Norwegian Krone"},
    "denmark": {"code": "DKK", "symbol": "kr", "name": "Danish Krone"},
    "finland": {"code": "EUR", "symbol": "€", "name": "Euro"},
    "argentina": {"code": "ARS", "symbol": "$", "name": "Argentine Peso"},
    "peru": {"code": "PEN", "symbol": "S/", "name": "Peruvian Sol"},
    "indonesia": {"code": "IDR", "symbol": "Rp", "name": "Indonesian Rupiah"},
    "philippines": {"code": "PHP", "symbol": "₱", "name": "Philippine Peso"},
    "qatar": {"code": "QAR", "symbol": "ر.ق", "name": "Qatari Riyal"},
    "saudi arabia": {"code": "SAR", "symbol": "﷼", "name": "Saudi Riyal"},
    "morocco": {"code": "MAD", "symbol": "د.م.", "name": "Moroccan Dirham"},
    "south africa": {"code": "ZAR", "symbol": "R", "name": "South African Rand"},
    "new zealand": {"code": "NZD", "symbol": "$", "name": "New Zealand Dollar"},
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


COUNTRY_ADJECTIVES = {
    "greece": "greek",
    "italy": "italian",
    "france": "french",
    "spain": "spanish",
    "portugal": "portuguese",
    "germany": "german",
    "austria": "austrian",
    "switzerland": "swiss",
    "united kingdom": "british",
    "ireland": "irish",
    "netherlands": "dutch",
    "belgium": "belgian",

    "united states": "american",
    "canada": "canadian",
    "mexico": "mexican",
    "brazil": "brazilian",
    "argentina": "argentinian",
    "peru": "peruvian",
    "colombia": "colombian",

    "japan": "japanese",
    "china": "chinese",
    "south korea": "korean",
    "india": "indian",
    "thailand": "thai",
    "vietnam": "vietnamese",
    "indonesia": "indonesian",
    "malaysia": "malaysian",

    "turkey": "turkish",
    "lebanon": "lebanese",
    "israel": "israeli",
    "egypt": "egyptian",
    "morocco": "moroccan",
    "tunisia": "tunisian",

    "australia": "australian",
    "new zealand": "new zealand",
}


STYLE_TO_TYPES = {
    "relaxed": [
        "cafe", "park", "spa", "library", "book_store", "aquarium", 
        "art_gallery", "botanical_garden", "movie_theater", "museum"
    ],
    "sightseeing": [
        "tourist_attraction", "museum", "church", "place_of_worship", 
        "hindu_temple", "synagogue", "mosque", "city_hall", "historical_landmark"
    ],
    "adventure": [
        "hiking_area", "natural_feature", "campground", "amusement_park", 
        "zoo", "stadium", "national_park", "adventure_sports_center"
    ],
    "food": [
        "restaurant", "bakery", "cafe", "meal_takeaway", "meal_delivery", 
        "liquor_store", "supermarket", "bar"
    ],
    "nightlife": [
        "bar", "night_club", "casino", "bowling_alley", "comedy_club", "liquor_store"
    ]
}



style_adjustments = {

    "relaxed": {
        "breakfast": +0.05,
        "activity": -0.05
    },

    "sightseeing": {
        "activity": +0.10,
        "lunch": -0.05,
        "nightlife": -0.05
    },

    "adventure": {
        "activity": +0.15,
        "dinner": -0.05,
        "nightlife": -0.10
    },

    "food": {
        "breakfast": +0.05,
        "lunch": +0.05,
        "dinner": +0.05,
        "activity": -0.10
    },

    "nightlife": {
        "nightlife": +0.20,
        "breakfast": -0.05,
        "activity": -0.05,
        "dinner": -0.10
    }
}


WEIGHTS_DISTRIBUTION = {
    "relaxed": {
        "p": 0.2,
        "d": 0.35,
        "r": 0.15,
        "n": 0.1,
        "s": 0.2
    },
    
    "sightseeing": {
        "p": 0.15,
        "d": 0.1,
        "r": 0.15,
        "n": 0.40,
        "s": 0.2
    },
    
    "adventure": {
        "p": 0.2,
        "d": 0.05,
        "r": 0.2,
        "n": 0.2,
        "s": 0.35
    },
    
    "food": {
        "p": 0.2,
        "d": 0.15,
        "r": 0.40,
        "n": 0.1,
        "s": 0.15
    },
    
    "nightlife": {
        "p": 0.15,
        "d": 0.25,
        "r": 0.2,
        "n": 0.15,
        "s": 0.25
    }
}



SPENDING_MODS = {
    "budget": {
        "p": +0.20,      
        "others": -0.05  
    },
    "balanced": {
        "p": 0.00, 
        "others": 0.00
    },

    "premium":  {
        "p": -0.10, 
        "r": 0.10
    },

    "luxury": {
        "p": -0.15,      
        "r": +0.10,      
        "s": +0.05       
    }
}



GOOGLE_PRICE_MAP = {
    "PRICE_LEVEL_FREE": 0,
    "PRICE_LEVEL_INEXPENSIVE": 1,
    "PRICE_LEVEL_MODERATE": 2,
    "PRICE_LEVEL_EXPENSIVE": 3,
    "PRICE_LEVEL_VERY_EXPENSIVE": 4
}


IDEAL_PRICE_MAP = {
    "budget": 1,   
    "balanced": 2,  
    "premium": 3,   
    "luxury": 4     
}

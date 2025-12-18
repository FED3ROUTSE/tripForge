import requests
import json
import os
from dotenv import load_dotenv
from urllib.parse import urlencode
from .data.city_data import CITY_TO_COUNTRY, COUNTRY_TO_CURRENCY

load_dotenv()

API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")

landmark = {
    "paris": "Eiffel Tower best view",
    "bucharest": "the colossal Palace of Parliament",
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

def get_place_photo(place):
    
    normalized_place = place.lower().strip()
    query = landmark.get(normalized_place)
    
    
    text_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": API_KEY
    }
    
    search = requests.get(text_url, params=params).json()
    results = search.get("results", [])

    if not results:
        print("No city results found.")
        return

    photos = results[0].get("photos")
    if not photos:
        print("No photos available for this city.")
        return

    photo_reference = photos[0].get("photo_reference")


    photo_url = "https://maps.googleapis.com/maps/api/place/photo"
    photo_params = {
        "maxwidth": 1600,  
        "maxheight": 600,   
        "photoreference": photo_reference,
        "key": API_KEY
    }

    photo_response = requests.get(photo_url, params=photo_params, allow_redirects=True, timeout=10)


    if photo_response.status_code == 200:
        final_url = photo_response.url
        print(f"Final Photo URL found: {final_url}")
        return final_url
    else:
        print(f"Photo API Error: HTTP {photo_response.status_code}")
        return None


def get_city_map_url(city_name):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    params = {
        "center": city_name,
        "zoom": 11,
        "size": "1600x600",
        "maptype": "roadmap",
        "key": os.environ.get("GOOGLE_PLACES_API_KEY"),
    }
    return base_url + urlencode(params)


def extract_trip_details(data):
    destination = data.get("destination")
    arrival = data.get("arrival")
    departure = data.get("departure")
    budget = data.get("budget")

    return {
        "destination": destination,
        "arrival": arrival,
        "departure": departure,
        "budget": budget
    }
    
    
def get_currencies(city):
    country = CITY_TO_COUNTRY.get(city.lower())
    return COUNTRY_TO_CURRENCY.get(country)
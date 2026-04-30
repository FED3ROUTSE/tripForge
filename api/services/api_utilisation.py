import requests
import json
import os
from dotenv import load_dotenv
from urllib.parse import urlencode
from ..data.city_data import (CITY_TO_COUNTRY, COUNTRY_TO_CURRENCY, COUNTRY_TO_PEAK_SEASON, COUNTRY_TO_POPULAR_ATTRACTIONS,
                             COUNTRY_TO_LOCAL_CUISINE, COUNTRY_ADJECTIVES, STYLE_TO_TYPES, style_adjustments, WEIGHTS_DISTRIBUTION,
                             SPENDING_MODS, LANDMARK)

load_dotenv()

API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")
UNSPLASH_KEY = os.environ.get("UNSPLASH_API_KEY")
UNSPLASH_BASE_URL = "https://api.unsplash.com"


def geocoding(destination):
    normalized_destination = destination.lower().strip()

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": normalized_destination,
        "key": API_KEY
    }

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()
    results = data.get("results", [])

    if not results:
        print("Destination not found!")
        return None

    location = results[0]["geometry"]["location"]

    if data.get("status") != "OK":
        print("Geocoding failed:", data.get("status"))
        return None

    return {
        "lat": location["lat"],
        "lng": location["lng"]
    }


def nearby_search(type, coordinations, radius):
    
    location = f"{coordinations['lat']},{coordinations['lng']}"

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": type,
        "key": API_KEY
    }

    res = requests.get(url, params=params).json()

    results = res.get("results", [])
    print("Status:", res["status"])
    print("Results:", len(results))
    
    filtered = []
    
    for p in results:
        types = p.get("types", [])
        
        if "fast_food_restaurant" in types or "meal_takeaway" in types:
            continue
        
        if "equipment" in types or "hotel" in types:
            continue
        
        filtered.append(p)
        
    sorted_best = sorted(filtered, key=lambda x: x.get("rating", 0), reverse=True)


    
    

def get_place_photo_google(place):
    
    normalized_place = place.lower().strip()
    query = LANDMARK.get(normalized_place)
    
    
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


def get_photo_unsplash(query):
    
    url = f"{UNSPLASH_BASE_URL}/search/photos"
    params = {
        "query": query,
        "per_page": 1,
        "orientation": "landscape",
        "client_id": UNSPLASH_KEY,
    }

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()
    if data["results"]:
        return data["results"][0]["urls"]["regular"]

    return None

def get_food_photo(food, adjective=None):
    food = food.strip().lower()

    base_url = f"{UNSPLASH_BASE_URL}/search/photos"

    queries = [
        f"{food}",                               
        f"{food} food",                 
        f"{adjective} {food}" if adjective else None,  
        f"{adjective} traditional food" if adjective else None,
        f"{food} traditional dish",              
        f"traditional food",                        
        f"local cuisine food",                       
    ]

    for query in queries:
        if not query:
            continue

        params = {
            "query": query,
            "per_page": 1,
            "orientation": "landscape",
            "client_id": UNSPLASH_KEY,
        }

        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()
        if data.get("results"):
            photo = data["results"][0]
            return {
                "url": photo["urls"]["regular"],
                "author": photo["user"]["name"],
                "username": photo["user"]["username"],
                "link": photo["links"]["html"],
                "query_used": query,  # optional but VERY useful for debugging
            }

    # Absolute fallback
    return None



def get_city_photo(city):
    
    city = city.strip().lower()
    url = f"{UNSPLASH_BASE_URL}/search/photos"
    params = {
        "query" : f"{city}",
        "per_page": 1,
        "orientation": "landscape",
        "client_id": UNSPLASH_KEY,
    }

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()
    if data["results"]:
        photo = data["results"][0]
        return {
        "url": photo["urls"]["regular"],
        "author": photo["user"]["name"],
        "username": photo["user"]["username"],
        "link": photo["links"]["html"],
    } 
        return None

def get_attraction_photo(attraction):
    
    attraction = attraction.strip().lower()
    url = f"{UNSPLASH_BASE_URL}/search/photos"
    params = {
        "query" : f"{attraction}",
        "per_page": 1,
        "orientation": "landscape",
        "client_id": UNSPLASH_KEY,
    }

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()
    if data["results"]:
        photo = data["results"][0]
        return {
        "url": photo["urls"]["regular"],
        "author": photo["user"]["name"],
        "username": photo["user"]["username"],
        "link": photo["links"]["html"],
    }

    return None





def nearby_search_refined(google_types, coordinations, radius=1000):
    url = "https://places.googleapis.com/v1/places:searchNearby"
 
    

    
    payload = {
        "includedPrimaryTypes": [google_types],
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": coordinations['lat'],
                    "longitude": coordinations['lng']
                },
                "radius": radius
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "*"
    }

    response = requests.post(url, json=payload, headers=headers)
    res_data = response.json()
    places = res_data.get("places", [])


    return places
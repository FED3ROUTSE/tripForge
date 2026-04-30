import requests
import json
import os
from dotenv import load_dotenv
from urllib.parse import urlencode
from ..data.city_data import (CITY_TO_COUNTRY, COUNTRY_TO_CURRENCY, COUNTRY_TO_PEAK_SEASON, COUNTRY_TO_POPULAR_ATTRACTIONS,
                             COUNTRY_TO_LOCAL_CUISINE, COUNTRY_ADJECTIVES, STYLE_TO_TYPES, style_adjustments, WEIGHTS_DISTRIBUTION,
                             SPENDING_MODS,)

load_dotenv()


BASE_ITINERARY = ["breakfast", "morning_activity", "lunch", "afternoon_activity", "dinner"]
ITINERARY_MODIFIERS = {
    "relaxed": {"action": "remove", "target": "afternoon_activity"},
    "nightlife": {"action": "append", "target": "drinks"}
}




base_distribution = {
    "breakfast": 0.15,
    "lunch": 0.25,
    "activity": 0.30,
    "dinner": 0.25,
    "nightlife": 0.05
}


    
    


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

def extract_travel_style(data):
    travel_style = data.get("travelStyle")
    
    return {
        "travel_style": travel_style,
    }
    
def extract_spending_style(data):
    spendingStyle = data.get("spendingStyle")
    
    return{
        "spendingStyle": spendingStyle
    }
    
    
def get_currencies(city):
    country = CITY_TO_COUNTRY.get(city.lower())
    return COUNTRY_TO_CURRENCY.get(country)

def get_country(city):
    return CITY_TO_COUNTRY.get(city.lower())

def get_peak_season(city):
    country = get_country(city)
    return COUNTRY_TO_PEAK_SEASON.get(country)

def is_month_in_range(month, start, end):
    if start <= end:
        return start <= month <= end
    return month >= start or month <= end

def get_attractions(country):
    return COUNTRY_TO_POPULAR_ATTRACTIONS.get(country, [])

def get_local_cuisine(country):
    return COUNTRY_TO_LOCAL_CUISINE.get(country, [])

def get_country_adjective(country: str):
    if not country:
        return None

    return COUNTRY_ADJECTIVES.get(country.strip().lower())





def get_active_weights(travel_style, spending_style):

    if isinstance(travel_style, str):
        travel_style = [travel_style]

    active = {"p": 0, "d": 0, "r": 0, "n": 0, "s": 0,}
    count = len(travel_style)

    for style_id in travel_style:
        style_row = WEIGHTS_DISTRIBUTION[style_id]
        for key in active:
            active[key] += style_row[key] / count

    mod = SPENDING_MODS.get(spending_style, SPENDING_MODS["balanced"])#

    for key, value in mod.items():
        if key == "others":
            for k in ["d", "r", "n", "s"]:
                active[k] += value
        else:
            active[key] += value

    return {k: max(0, v) for k, v in active.items()}

def get_google_types(user_styles):
    styles = STYLE_TO_TYPES
    track_types = []
    
    for style in user_styles:
        track = styles.get(style, [])
        track_types.append(track)
    
    flatList = []

    for element in track_types:
        if type(element) is list:
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList


def build_daily_schedule(user_styles):
    itinerary = BASE_ITINERARY.copy()
    modify = ITINERARY_MODIFIERS
    for style in user_styles:
        if style in modify:
            rule = modify[style]
            action = rule.get("action")
            target = rule.get("target")
            if action == "remove":
                itinerary.remove(target)
            elif action == "append":
                itinerary.append(target)
    return itinerary

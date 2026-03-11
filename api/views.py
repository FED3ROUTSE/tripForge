from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import (
    extract_trip_details, extract_travel_style, get_place_photo_google, get_city_map_url, get_photo_unsplash, get_city_photo,
    get_currencies, get_country, get_peak_season, is_month_in_range, get_attractions, get_local_cuisine,
    get_attraction_photo, get_food_photo, get_country_adjective, geocoding, nearby_search, extract_spending_style)
from datetime import date
from datetime import datetime
import pandas as pd

@api_view(["POST"])
def plan_trip(request):
    data = request.data

    trip_details = extract_trip_details(data)
    destination = trip_details.get("destination")
    arrival = trip_details.get("arrival")
    departure = trip_details.get("departure")
    budget = trip_details.get("budget")
    print("Destination:", destination)
    print("Arrival:", arrival)
    print("Departure:", departure)
    print("Budget:", budget)
    
    city_map = get_city_map_url(destination)
    print("City map: ", city_map)
    photo_url = get_place_photo_google(destination)
    
    
    d1 = datetime.strptime(departure, "%Y-%m-%d")
    d2 = datetime.strptime(arrival, "%Y-%m-%d")
    duration_days = (d1-d2).days
    print("Duration in days:", duration_days)
    
    daily_budget = budget/duration_days
    format_budget = f"{daily_budget:.2f}"
    print(f"Daily budget: {format_budget}")
    
    currency = get_currencies(destination)
    name = currency
    print("Currency:", currency)
    
    country = get_country(destination)
    
    peak_season = get_peak_season(destination)
    print("Off season:", peak_season)
    arrival_date = datetime.strptime(arrival, "%Y-%m-%d")
    departure_date = datetime.strptime(departure, "%Y-%m-%d")
    departure_month = departure_date.month
    arrival_month = arrival_date.month
    is_peak_season = any(
    is_month_in_range(arrival_month, start, end)
    for start, end in peak_season
    )
    season_label = "Peak season" if is_peak_season else "Off-peak season"
    print("Season:", season_label)

    attractions = get_attractions(country)
    local_cuisine = get_local_cuisine(country)
    
    print("Local Cuisine:", local_cuisine)
    print("Popular attractions:", attractions)
    attraction_photos = {}
    food_photos = {}

    for attraction in attractions:
        photo = get_attraction_photo(attraction)
        if photo:
            attraction_photos[attraction] = photo

    for food in local_cuisine:
        photo = get_food_photo(food)
        if photo:
            food_photos[food] = photo
        
    city_photo = get_city_photo(destination)
    
    adjective = get_country_adjective(country)
    
    print("City photo ULR", city_photo)
    print("Attractions photo ULR",attraction_photos)
    print("Food photo ULR",food_photos)

    
    
    return Response({
    "success": True,
    "destination": destination,
    "arrival": arrival,
    "departure": departure,
    "budget": budget,
    "city_map": city_map,
    "duration_days": duration_days,
    "format_budget": format_budget,
    "currency": currency,
    "season_label": season_label,
    "city_photo": city_photo,  
    "food_photos": food_photos,
    "attraction_photos": attraction_photos,
})
    
@api_view(["POST"])
def plan_style(request):
    
    data = request.data
    travel_style = extract_travel_style(data)
    spendingStyle = extract_spending_style(data)
    trip_details = extract_trip_details(data)
    destination = trip_details.get("destination")
    arrival = trip_details.get("arrival")
    departure = trip_details.get("departure")
    budget = trip_details.get("budget")
    print("Destination:", destination)
    print("Arrival:", arrival)
    print("Departure:", departure)
    print("Budget:", budget)
    
    d1 = datetime.strptime(departure, "%Y-%m-%d")
    d2 = datetime.strptime(arrival, "%Y-%m-%d")
    duration_days = (d1-d2).days
    print("Duration in days:", duration_days)
    
    daily_budget = budget/duration_days
    format_budget = f"{daily_budget:.2f}"
    
        
    day = list(range(1, duration_days + 1))
    
    print("Days: ", day)
    print("Travel Style:", travel_style)
    print("Spending Style:", spendingStyle)

    coordinates = geocoding(destination)
    
    
    return Response({
        "success": True,
        "travel_style": travel_style,
        "spendingStyle": spendingStyle,
        "destination": destination,
        "arrival": arrival,
        "departure": departure,
        "day": day,
        "budget": budget,
        "duration_days": duration_days,
        "format_budget": format_budget,
        
    })
    



from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import (
    extract_trip_details, get_place_photo_google, get_city_map_url, get_photo_unsplash,
    get_currencies, get_country, get_peak_season, is_month_in_range, get_attractions, get_local_cuisine)
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
    photo_url = get_place_photo(destination)
    
    
    d1 = datetime.strptime(departure, "%Y-%m-%d")
    d2 = datetime.strptime(arrival, "%Y-%m-%d")
    duration_days = (d1-d2).days
    print("Duration in days:", duration_days)
    
    daily_budget = budget/duration_days
    print(f"Daily budget: {daily_budget:.2f}")
    
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
    
    return Response({
    "success": True,
    "destination": destination,
    "arrival": arrival,
    "departure": departure,
    "budget": budget,
    "city_map": city_map,
    "duration_days": duration_days,
    "daily_budget": daily_budget,
    "currency": currency,
    "season_label": season_label,
    "attractions": attractions,
    "local_cuisine": local_cuisine,
})
    



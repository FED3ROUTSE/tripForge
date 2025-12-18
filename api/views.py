from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import extract_trip_details, get_place_photo, get_city_map_url, get_currencies
from datetime import date
from datetime import datetime

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

    return Response({
    "success": True,
    "destination": destination,
    "arrival": arrival,
    "departure": departure,
    "budget": budget,
    "city_map": city_map,
    "duration_days": duration_days,
    "daily_budget": daily_budget,
    "currency": currency
})
    



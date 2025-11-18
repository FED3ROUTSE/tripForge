from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def plan_trip(request):
    data = request.data  # This is the JSON from React
    print("Received trip data:", data)  # <-- print to console

    # You can access individual fields
    destination = data.get("destination")
    arrival = data.get("arrival")
    departure = data.get("departure")
    budget = data.get("budget")

    print(f"Destination: {destination}, Arrival: {arrival}, Departure: {departure}, Budget: {budget}")

    return Response({
        "success": True,
        "received": data
    })



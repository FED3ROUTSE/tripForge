def calculate_total_score(place_data, user_prefs, weights):
    user_travel_style = user_prefs.get("selected_styles", [])
    user_spending_style = user_prefs.get("spending_style", [])
    user_lat = user_prefs.get("lat", [])
    user_lng = user_prefs.get("lng", [])
    
    google_types = place_data.get("types", [])
    google_price = place_data.get("price_level", [])
    google_rating = place_data.get("rating", [])
    google_total_rating = place_data.get("user_ratings_total", [])
    google_lat = place_data.get("geometry", []).get("location", []).get("lat", [])
    google_lng = place_data.get("geometry", []).get("location", []).get("lng", [])
    return None
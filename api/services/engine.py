from api.services.normalizers import *

# weights is get_active weights which will be calculated in view and passed as parameter
def calculate_total_score(place_data, user_prefs, weights):
    user_travel_style = user_prefs.get("selected_styles", [])
    user_spending_style = user_prefs.get("spending_style", [])
    user_lat = user_prefs.get("lat")
    user_lng = user_prefs.get("lng")
    
    google_types = place_data.get("types", [])
    google_price = place_data.get("price_level", 0)
    google_rating = place_data.get("rating", 0)
    google_popularity = place_data.get("user_ratings_total", 0.0)
    google_lat = place_data.get("geometry", {}).get("location", {}).get("lat", None)
    google_lng = place_data.get("geometry", {}).get("location", {}).get("lng", None)
    
    score_price = normalize_price(google_price, user_spending_style)
    score_distance = normalize_distance(user_lat, user_lng, google_lat, google_lng)
    score_rating = normalize_rating(google_rating)
    score_popularity = normalize_popularity(google_popularity)
    score_match = normalize_style_match(google_types, user_travel_style)
    
    score = {
        "p": score_price,
        "d": score_distance,
        "r": score_rating,
        "n": score_popularity,
        "s": score_match
    }
    
    total_score = ((weights.get("p") * score["p"]) + (weights.get("d") * score["d"])
    + (weights.get("r") * score["r"]) + (weights.get("n") * score["n"])
    + (weights.get("s") * score["s"]))
    
    total_weights = sum(weights.values())
    
    if total_weights > 0:
        final_score = total_score/total_weights
    return final_score
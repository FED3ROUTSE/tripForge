from ..data.city_data import GOOGLE_PRICE_MAP, IDEAL_PRICE_MAP, STYLE_TO_TYPES
import math

def normalize_price(google_price_string, user_spending_style):

    actual_level = GOOGLE_PRICE_MAP.get(google_price_string, 2)

    ideal_level = IDEAL_PRICE_MAP.get(user_spending_style, 2)

    diff = abs(actual_level - ideal_level)
    
    score = max(0.1, 1.0 - (diff * 0.3))
    
    return score

def normalize_distance(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    a = (pow(math.sin(dLat / 2), 2) + 
         pow(math.sin(dLon / 2), 2) * 
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    distance = rad * c

    max_threshold = 5.0

    score = max(0.1 , 1.0 -(distance / max_threshold))

    return score

def normalize_rating(rating):
    if rating == None or rating <= 0.0 :
        rating = 2.5

    rating = float(rating)
    rating = rating / 5.0

    return rating

def normalize_popularity(review_count):
    if review_count == None or review_count <= 0:
        review_count = 0.1
    
    review_count = float(review_count)

    max_threshold = 5000.0

    score = max(0.1 , math.log10(review_count) / math.log10(max_threshold))

    score = min(score, 1)

    return score

def normalize_style_match(google_place_types, user_styles):
    styles = STYLE_TO_TYPES

    for style in user_styles:
        track = styles.get(style, [])
        for place_type in google_place_types:
            if place_type in track:
                return 1.0
    return 0.0
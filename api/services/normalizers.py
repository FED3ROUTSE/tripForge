from ..data.city_data import GOOGLE_PRICE_MAP, IDEAL_PRICE_MAP
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

    max_threshold = 5

    score = max(0.1 , 1.0 -(distance / max_threshold))

    return score
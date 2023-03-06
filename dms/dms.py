from flask import Flask, request, jsonify
import math
import h3
import random
import time
from datetime import datetime, timezone
import threading
import time
from random import randint

from reviews import get_random_review
import os
import redis
import json


r = redis.Redis(host='redis', port=6379)
    

DYNAMIC_RATE_PER_KM = os.environ.get('DYNAMIC_RATE_PER_KM', 'False').lower() == 'true'
REVIEWS_PER_PAGE = 100

app = Flask(__name__)

fleet_prices = {
    'fleet_1': 2.7,
    'fleet_2': 3.1,
    'fleet_3': 3.7,
    'fleet_4': 3.5,
    'fleet_5': 2.8,
    'fleet_6': 2.1,
    'fleet_7': 1.8,
    'fleet_8': 2.8,
    'fleet_9': 3.1,
    'fleet_10': 3.9,
}

london_center = (51.5115458,-0.1588615)
london_resolution = 4
london_coverage_h3_cell = h3.geo_to_h3(london_center[0], london_center[1], london_resolution)
print("London h3 cell: {}".format(london_coverage_h3_cell))

def update_rates():
    while True:
        fleet = "fleet_{}".format(random.randint(1, 10))
        fleet_prices[fleet] += 0.20
        time.sleep(10)

if DYNAMIC_RATE_PER_KM:
    t = threading.Thread(target=update_rates)
    t.start()

@app.route('/price', methods=['POST'])
def get_price():
    data = request.get_json()

    # Check if request is within London h3 cell
    pickup_h3 = h3.geo_to_h3(data['pickup_lat'], data['pickup_lng'], london_resolution)
    dropoff_h3 = h3.geo_to_h3(data['dropoff_lat'], data['dropoff_lng'], london_resolution)
    london_h3 = h3.geo_to_h3(*london_center, london_resolution)
    if pickup_h3 != london_h3 or dropoff_h3 != london_h3:
        return jsonify({'error': 'Request must be within London h3 cell of resolution {}'.format(london_resolution)}), 400

    # Check if fleet name is valid
    if data['fleet_name'] not in fleet_prices:
        return jsonify({'error': 'Invalid fleet name'}), 400

    # Calculate distance between pickup and dropoff using haversine formula
    pickup = (data['pickup_lat'], data['pickup_lng'])
    dropoff = (data['dropoff_lat'], data['dropoff_lng'])
    distance_km = haversine(pickup, dropoff)

    # Calculate price based on fleet price per kilometer
    fleet_price = fleet_prices[data['fleet_name']]

    rating = sum(fleet_ratings[data['fleet_name']])/len(fleet_ratings[data['fleet_name']])
    price = distance_km * fleet_price + (rating-5) * 0.3

    # Return price as JSON response
    return jsonify({'price': price, 'rating': rating, 'distance': distance_km, 'description': get_fleet_description(data['fleet_name'])})

def haversine(point1, point2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lat1, lon1 = point1
    lat2, lon2 = point2

    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

fleet_bases = {}

places = [
    ["Buckingham Palace", [51.5014, -0.1419]],
    ["Tower Bridge", [51.5055, -0.0754]],
    ["The British Museum", [51.5194, -0.1269]],
    ["The Shard", [51.5045, -0.0865]],
    ["Kensington Palace", [51.5051, -0.1877]],
    ["Westminster Abbey", [51.4994, -0.1276]],
    ["The Tower of London", [51.5081, -0.0759]],
    ["St. Paul's Cathedral", [51.5138, -0.0984]],
    ["Tate Modern", [51.5076, -0.0994]],
    ["The Royal Observatory, Greenwich", [51.4778, -0.0015]]
]

for i in range(10):
    fleet_bases["fleet_{}".format(i+1)] = places[i][1]

def get_fleet_description(fleet_name):
    return "Taxi fleet based in {}".format(places[int(fleet_name.split('_')[1])-1][0])

def random_point_around(center, radius_km):
    lat, lng = center
    r = radius_km / 111300 # = 100 meters

    u = random.random()
    v = random.random()

    w = r * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    return (lat + y, lng + x)


def generate_review(fleet):
    fleet_base = fleet_bases[fleet]
    pickup_lat, pickup_lng = random_point_around(london_center, 10)
    dropoff_lat, dropoff_lng = random_point_around(london_center, 10)

    pickup_distance_from_base = haversine(fleet_base, (pickup_lat, pickup_lng))
    dropoff_distance_from_base = haversine(fleet_base, (dropoff_lat, dropoff_lng))

    # we assume fleet rating decreases based on the distance from the fleet base
    # as the driver doesn't know the areas as well. Pickup distance matters more
    distance_heuristic = pickup_distance_from_base*0.8 + dropoff_distance_from_base*0.2
    rating = max(min(round(5 - 5*(distance_heuristic/18)), 5), 1)
    (text, rating) = get_random_review(rating)
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return Review(text, rating, fleet, current_time, pickup_lat, pickup_lng, dropoff_lat, dropoff_lng)

fleet_ratings = {
    "fleet_1": [],
    "fleet_2": [],
    "fleet_3": [],
    "fleet_4": [],
    "fleet_5": [],
    "fleet_6": [],
    "fleet_7": [],
    "fleet_8": [],
    "fleet_9": [],
    "fleet_10": []
}

def get_ratings():
    return {fleet: sum(ratings) / len(ratings) if len(ratings) > 0 else 0 for fleet, ratings in fleet_ratings.items()}

class Review:
    def __init__(self, text, rating, fleet, review_time, pickup_lat, pickup_lng, destination_lat, destination_lng):
        self.text = text
        self.rating = rating
        self.fleet = fleet
        self.review_time = review_time
        self.pickup_lat = pickup_lat
        self.pickup_lng = pickup_lng
        self.destination_lat = destination_lat
        self.destination_lng = destination_lng

reviews = []

def create_reviews():
    while True:
        for _ in range(10):
            fleet = "fleet_{}".format(random.randint(1, 10))
            review = generate_review(fleet)
            reviews.insert(0, review)
            fleet_ratings[fleet].insert(0, review.rating)
            if len(fleet_ratings[fleet]) > 10:
                fleet_ratings[fleet].pop()

            r.publish('reviews-channel', json.dumps(review))
        time.sleep(1)
# create_reviews()

review_thread = threading.Thread(target=create_reviews)
review_thread.start()

@app.route('/reviews')
def get_reviews():
    page = int(request.args.get('page', 1))
    start_idx = (page - 1) * REVIEWS_PER_PAGE
    end_idx = start_idx + REVIEWS_PER_PAGE
    paged_reviews = reviews[start_idx:end_idx]
    return jsonify({
        'reviews': [{'text': r.text, 'rating': r.rating, 'fleet': r.fleet} for r in paged_reviews],
            })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# DMS simulator which also provides fleet reviews

```
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"pickup_lat": 51.5074, "pickup_lng": -0.1278, "dropoff_lat": 51.5285, "dropoff_lng": -0.0847, "fleet_name": "fleet_1"}' \
     http://localhost:8000/price
```

```
curl http://localhost:8000/reviews\?page\=3
```

Reviews are published in Redis on `reviews-channel`

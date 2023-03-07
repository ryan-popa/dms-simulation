import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# Define the list of well-known London places
london_places = {
    "Buckingham Palace": (51.5014, -0.1419),
    "London Eye": (51.5033, -0.1195),
    "Tower Bridge": (51.5055, -0.0754),
    "Big Ben": (51.5007, -0.1246),
}

st.title("London Taxi Fare Estimator")

# Define the dropdown menus for pickup and dropoff
c1, c2 = st.columns(2)
with c1:
    pickup = st.selectbox("Pickup", list(london_places.keys()))
with c2:
    dropoff = st.selectbox(
        "dropoff", list([e for e in london_places.keys() if e != pickup])
    )

# Get the latitude and longitude of the selected pickup and dropoff
pickup_lat, pickup_lng = london_places[pickup]
dropoff_lat, dropoff_lng = london_places[dropoff]

# Create a folium map object
m = folium.Map(location=[pickup_lat, pickup_lng], zoom_start=12)

# Add the pickup and dropoff markers to the map
folium.Marker([pickup_lat, pickup_lng], popup="Pickup Location").add_to(m)
folium.Marker([dropoff_lat, dropoff_lng], popup="dropoff Location").add_to(m)

# Add an arch between the pickup and dropoff locations
folium.PolyLine(
    locations=[[pickup_lat, pickup_lng], [dropoff_lat, dropoff_lng]],
    weight=5,
    color="blue",
).add_to(m)

# Render the map in Streamlit
st_folium(m, zoom=14, height=300, width=800)

# Calculate the fare and rating based on the entered coordinates
if st.button("Calculate"):
    # Make a request to the price service with the entered coordinates
    response = requests.post(
        "http://karhoo:5000/best_price",
        json={
            "pickup_lat": pickup_lat,
            "pickup_lng": pickup_lng,
            "dropoff_lat": dropoff_lat,
            "dropoff_lng": dropoff_lng,
        },
        headers={"Content-Type": "application/json"},
    )

    # Parse the response and display the fare and rating
    if response.status_code == 200:
        price = response.json()["best_price"]
        rating = response.json()["rating"]
        fleet = response.json()["fleet"]
        st.write(f"Price: {price}")
        st.write(f"Rating: {rating}")
        st.write(f"Fleet: {fleet}")
    else:
        st.write("Error calculating price")
        st.write(response.text)

import os
import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

# database configuration
db_host = os.environ.get("DB_HOST", "db")
db_name = os.environ.get("DB_NAME", "database")
db_user = os.environ.get("DB_USER", "user")
db_password = os.environ.get("DB_PASSWORD", "password")
print(db_host, db_name, db_user, db_password)
# raise Exception('test')

# Connect to the database
mydb = mysql.connector.connect(
    host=db_host, user=db_user, password=db_password, database=db_name
)

# Check if connection was successful
if mydb.is_connected():
    print("Connected to MySQL database")

cursor = mydb.cursor()

# migration to create "reviews" table

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS reviews (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        pickup_lat FLOAT(10,6) NOT NULL,
        pickup_lng FLOAT(10,6) NOT NULL,
        dropoff_lat FLOAT(10,6) NOT NULL,
        dropoff_lng FLOAT(10,6) NOT NULL,
        review_time TIME NOT NULL,
        fleet VARCHAR(255) NOT NULL,
        text VARCHAR(255) NOT NULL,
        review INT(11) NOT NULL,
        trip_id VARCHAR(255) NOT NULL
    );
"""
)


# endpoint to get best price for route
@app.route("/best_price", methods=["POST"])
async def get_best_price():
    data = request.get_json()
    pickup_lat = data.get("pickup_lat")
    pickup_lng = data.get("pickup_lng")
    dropoff_lat = data.get("dropoff_lat")
    dropoff_lng = data.get("dropoff_lng")

    # calculate best price based on route
    best_price = 10.0  # example value
    response_data = {"best_price": best_price, "rating": 4.5, "fleet": "uber"}
    return jsonify(response_data)


# endpoint to get current score for each fleet
@app.route("/fleet_reviews")
def get_fleet_reviews():
    cursor.execute(
        """
        SELECT fleet, AVG(review) AS avg_review
        FROM reviews
        GROUP BY fleet
    """
    )
    results = cursor.fetchall()
    response_data = [
        {"fleet": result["fleet"], "score": result["avg_review"]} for result in results
    ]
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

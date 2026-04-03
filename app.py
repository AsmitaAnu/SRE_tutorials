from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data (like a mini database)
trips = [
    {"id": 1, "destination": "Goa", "price": 5000},
    {"id": 2, "destination": "Manali", "price": 7000},
    {"id": 3, "destination": "Kerala", "price": 6500}
]

bookings = []

# Home route
@app.route('/')
def home():
    return "Travel Booking API is running, we are travelling to Dubai ✈️"

# Get all trips
@app.route('/trips', methods=['GET'])
def get_trips():
    return jsonify(trips)

# Book a trip
@app.route('/book', methods=['POST'])
def book_trip():
    data = request.get_json()
    trip_id = data.get("trip_id")
    user = data.get("user")

    for trip in trips:
        if trip["id"] == trip_id:
            booking = {"user": user, "trip": trip}
            bookings.append(booking)
            return jsonify({"message": "Booking successful 🎉", "booking": booking})

    return jsonify({"error": "Trip not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

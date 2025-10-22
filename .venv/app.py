from flask import Flask, jsonify, request

app = Flask(__name__)

sensor_data = [
    {
        "timestamp": "2023-05-28T10:30:00",
        "temperature": 25.5,
        "humidity": 60.2,
        "pressure": 1012.3
    },
    {
        "timestamp": "2023-05-28T10:35:00",
        "temperature": 25.8,
        "humidity": 59.8,
        "pressure": 1012.7
    },
    {
        "timestamp": "2023-05-28T10:40:00",
        "temperature": 26.1,
        "humidity": 59.5,
        "pressure": 1012.9
    }
]

# Task 1: Retrieve average temperature
@app.route('/average-temperature', methods=['GET'])
def get_average_temperature():
    # TODO: Implement code to calculate the average temperature
    # and return it as a JSON response
    pass

# Task 2: Add a new sensor data entry
@app.route('/sensor-data', methods=['POST'])
def add_sensor_data():
    # TODO: Implement code to add a new sensor data entry
    # based on the request body JSON
    pass

# Task 3: Update an existing sensor data entry by timestamp
@app.route('/sensor-data/<timestamp>', methods=['PUT'])
def update_sensor_data(timestamp):
    # TODO: Implement code to update an existing sensor data entry
    # based on the provided timestamp and request body JSON
    pass

if __name__ == '__main__':
    app.run(debug=True)

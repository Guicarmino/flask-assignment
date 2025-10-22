from flask import Flask, jsonify, request

app = Flask(__name__)

# -------- Seed data --------
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

# -------- Simple home/health route (for browser test) --------
@app.get("/")
def health():
    return jsonify({"status": "ok"})

# -------- Task 1: Retrieve average temperature --------
@app.get("/average-temperature")
def get_average_temperature():
    if not sensor_data:
        return jsonify({"average_temperature": None, "count": 0, "unit": "C"}), 200

    avg = sum(item["temperature"] for item in sensor_data) / len(sensor_data)
    return jsonify({
        "average_temperature": round(avg, 2),
        "count": len(sensor_data),
        "unit": "C"
    }), 200

# (bonus helper) get all sensor data for quick checks
@app.get("/sensor-data")
def list_sensor_data():
    return jsonify(sensor_data), 200

# -------- Task 2: Add a new sensor data entry --------
@app.post("/sensor-data")
def add_sensor_data():
    data = request.get_json(silent=True) or {}

    required = {"timestamp", "temperature", "humidity", "pressure"}
    missing = [k for k in required if k not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Basic type checks (lightweight)
    try:
        float(data["temperature"])
        float(data["humidity"])
        float(data["pressure"])
    except (TypeError, ValueError):
        return jsonify({"error": "temperature, humidity, and pressure must be numeric"}), 400

    # Add to in-memory list
    sensor_data.append({
        "timestamp": data["timestamp"],
        "temperature": float(data["temperature"]),
        "humidity": float(data["humidity"]),
        "pressure": float(data["pressure"])
    })

    return jsonify({"message": "created", "size": len(sensor_data)}), 201

# -------- Task 3: Update an existing entry by timestamp --------
@app.put("/sensor-data/<timestamp>")
def update_sensor_data(timestamp):
    body = request.get_json(silent=True) or {}

    # Find the entry by exact timestamp match
    for item in sensor_data:
        if item["timestamp"] == timestamp:
            # Update only provided fields
            for key in ("temperature", "humidity", "pressure"):
                if key in body:
                    try:
                        item[key] = float(body[key])
                    except (TypeError, ValueError):
                        return jsonify({"error": f"{key} must be numeric"}), 400
            # Optionally allow timestamp change too
            if "timestamp" in body:
                item["timestamp"] = body["timestamp"]
            return jsonify({"message": "updated", "item": item}), 200

    return jsonify({"error": f"timestamp '{timestamp}' not found"}), 404


if __name__ == "__main__":
    # host=0.0.0.0 is important for Codespaces port forwarding
    app.run(host="0.0.0.0", port=5000, debug=True)

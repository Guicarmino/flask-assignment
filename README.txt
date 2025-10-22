Run steps:
1) python3 -m venv .venv
2) source .venv/bin/activate
3) pip install -r requirements.txt
4) python app.py
API:
GET /               -> {"status":"ok"}
GET /sensor-data
GET /average-temperature
POST /sensor-data   -> JSON body with timestamp, temperature, humidity, pressure
PUT /sensor-data/<timestamp> -> JSON body to update fields

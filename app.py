from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Mock data representing properties and their availability
properties = [
    {"id": 1, "name": "Cozy City Apartment", "available_from": "2024-09-01", "available_to": "2024-09-30"},
    {"id": 2, "name": "Beachfront Villa", "available_from": "2024-09-15", "available_to": "2024-10-15"},
    {"id": 3, "name": "Mountain Cabin", "available_from": "2024-09-05", "available_to": "2024-09-20"},
]

def is_available(property, start_date, end_date):
    """Checks if the property is available within the given date range."""
    available_from = datetime.strptime(property["available_from"], "%Y-%m-%d")
    available_to = datetime.strptime(property["available_to"], "%Y-%m-%d")
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return available_from <= start and available_to >= end

@app.route('/')
def index():
    """Render the preview page."""
    return render_template('index.html')

@app.route('/api/availability', methods=['GET'])
def check_availability():
    # Get the start and end dates from the query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Validate dates
    if not start_date or not end_date:
        return jsonify({'error': 'Please provide both start_date and end_date in YYYY-MM-DD format'}), 400
    
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD format.'}), 400

    # Find available properties within the specified date range
    available_properties = [property for property in properties if is_available(property, start_date, end_date)]

    return jsonify({'available_properties': available_properties}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


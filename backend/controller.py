from flask import Flask, request, jsonify
from flask_cors import CORS
from repository import *
from pathlib import Path
import os

app = Flask(__name__)
CORS(app)
log = app.logger


# Health Check Route
@app.route('/status', methods=['GET'])
def status():
    raw_data = Path(os.getenv('DB_PATH', default='db.json'))
    if raw_data.is_file():
        health_check = jsonify(status='UP'), 200
        log.info('Application is UP')
    else:
        health_check = jsonify(status='DOWN'), 500
        log.error('Application is DOWN')
    return health_check


# Hotels Routes
@app.route('/hotels', methods=['GET'])
def get_hotels():

    hotels = find_hotels()

    if not hotels:
        log.warn('No hotels were found')
        return jsonify([]), 404

    return jsonify(hotels), 200


@app.route('/hotels/<hotel_id>', methods=['GET'])
def get_hotel(hotel_id):

    hotel = find_hotel(hotel_id)

    if not hotel:
        log.warn(f'Hotel {hotel_id} not found')
        return jsonify({"error": "hotel not found"}), 404

    return jsonify(hotel), 200


@app.route('/hotels', methods=['POST'])
def add_hotel():

    created = create_hotel(request.json)

    return jsonify(created), 201


@app.route('/hotels/<hotel_id>', methods=['PUT'])
def edit_hotel(hotel_id):

    edited_hotel = update_hotel(hotel_id, request.json)

    if not edited_hotel:
        log.warn(f'Hotel {hotel_id} not found to be edited')
        return jsonify({"error": "hotel not found to be edited"}), 404

    return jsonify(edited_hotel), 200


@app.route('/hotels/<hotel_id>', methods=['DELETE'])
def remove_hotel(hotel_id):

    deleted = delete_hotel(hotel_id)

    if not deleted:
        log.warn(f'Hotel {hotel_id} not found to be deleted')
        return jsonify({"error": "hotel not found to be deleted"}), 404

    return jsonify(''), 204

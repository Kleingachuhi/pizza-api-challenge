from flask import Blueprint, jsonify
from server.models import Restaurant
from server import db

restaurants_bp = Blueprint('restaurants_bp', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    response = [r.to_dict() for r in restaurants]
    return jsonify(response), 200

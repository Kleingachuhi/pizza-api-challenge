from flask import Blueprint, jsonify
from server.models import Restaurant
from server import db

restaurants_bp = Blueprint('restaurants_bp', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    response = [r.to_dict() for r in restaurants]
    return jsonify(response), 200

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify(restaurant.to_dict()), 200
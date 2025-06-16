from flask import Blueprint, jsonify, abort
from ..models import Restaurant, db
from sqlalchemy.exc import SQLAlchemyError

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        restaurants = Restaurant.query.all()
        return jsonify([restaurant.to_dict() for restaurant in restaurants]), 200
    except SQLAlchemyError:
        abort(500, description="Database error occurred")

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        abort(404, description="Restaurant not found")
    return jsonify(restaurant.to_dict_with_pizzas()), 200

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            abort(404, description="Restaurant not found")
        
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, description="Database error occurred")
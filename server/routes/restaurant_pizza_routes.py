from server import db
from flask import Blueprint, request, jsonify, abort
from server.models import RestaurantPizza, Restaurant, Pizza
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

# Add GET endpoint to fetch all restaurant_pizza associations
@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['GET'])
def get_restaurant_pizzas():
    try:
        restaurant_pizzas = RestaurantPizza.query.all()
        return jsonify([{
            "id": rp.id,
            "price": rp.price,
            "pizza": rp.pizza.to_dict(),
            "restaurant": rp.restaurant.to_dict()
        } for rp in restaurant_pizzas]), 200
    except SQLAlchemyError:
        abort(500, description="Database error occurred")

# Keep existing POST endpoint for creating new associations
@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    if not data or not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
        abort(400, description="Missing required fields")
    
    try:
        price = int(data['price'])
        if not 1 <= price <= 30:
            abort(400, description="Price must be between 1 and 30")
    except ValueError:
        abort(400, description="Price must be an integer")

    try:
        restaurant = Restaurant.query.get(data['restaurant_id'])
        pizza = Pizza.query.get(data['pizza_id'])
        
        if not restaurant or not pizza:
            abort(404, description="Restaurant or Pizza not found")

        restaurant_pizza = RestaurantPizza(
            price=price,
            restaurant_id=data['restaurant_id'],
            pizza_id=data['pizza_id']
        )

        db.session.add(restaurant_pizza)
        db.session.commit()

        return jsonify({
            "id": restaurant_pizza.id,
            "price": restaurant_pizza.price,
            "pizza": pizza.to_dict(),
            "restaurant": restaurant.to_dict()
        }), 201

    except IntegrityError:
        db.session.rollback()
        abort(400, description="This pizza-restaurant combination already exists")
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, description="Database error occurred")
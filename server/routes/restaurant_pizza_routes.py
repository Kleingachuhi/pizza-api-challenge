from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, Restaurant, Pizza
from server import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    
    if not data or not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    try:
        price = int(data['price'])
        if not 1 <= price <= 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    except ValueError:
        return jsonify({"errors": ["Price must be a number"]}), 400

    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])
    if not pizza or not restaurant:
        return jsonify({"errors": ["Pizza or restaurant not found"]}), 404

    try:
        new_rp = RestaurantPizza(
            price=price,
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()
        
        return jsonify(pizza.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
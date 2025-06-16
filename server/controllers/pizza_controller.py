from flask import Blueprint, jsonify, abort
from ..models import Pizza, db
from sqlalchemy.exc import SQLAlchemyError

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    try:
        pizzas = Pizza.query.all()
        return jsonify([pizza.to_dict() for pizza in pizzas]), 200
    except SQLAlchemyError:
        abort(500, description="Database error occurred")
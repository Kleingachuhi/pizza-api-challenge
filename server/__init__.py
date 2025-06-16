from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from .models.pizza import Pizza
from .models.restaurant import Restaurant
from .models.restaurant_pizza import RestaurantPizza

def create_app():
    """Factory function to create Flask app"""
    from .app import create_app
    return create_app()
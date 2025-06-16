from flask import Flask
from .config import Config
from . import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from server.routes.restaurant_routes import restaurant_bp
    from server.routes.pizza_routes import pizza_bp
    from server.routes.restaurant_pizza_routes import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app
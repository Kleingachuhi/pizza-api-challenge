from flask import Flask, config
from flask_sqlalchemy import SQLALCHEMY
from flask_migrate import Migrate
from .config import Config


db = SQLALCHEMY()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . controllers.restaurant_controller import restaurant_bp
    from .controllers.pizza_controller import pizza_bp
    from . controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)


    return app
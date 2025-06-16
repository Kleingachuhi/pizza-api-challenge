from .restaurants import restaurants_bp

def register_routes(app):
    app.register_blueprint(restaurants_bp)

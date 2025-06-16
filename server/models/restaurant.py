from server import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }

    def to_dict_with_pizzas(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": [
                {
                    "id": rp.pizza.id,
                    "name": rp.pizza.name,
                    "ingredients": rp.pizza.ingredients
                } for rp in self.restaurant_pizzas
            ]
        }

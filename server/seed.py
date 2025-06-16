from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza


app = create_app()

with app.app_context():
    print("Seeding database...")

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    r1 = Restaurant(name="Mama Oliech's Kitchen", address="15 Rose Avenue, Nairobi")
    r2 = Restaurant(name="Nyayo Pizza Spot", address="202 Kenyatta Road, Nakuru")

    p1 = Pizza(name="Nyama Feast", ingredients="Tomato Sauce, Mozzarella, Beef, Sukuma Wiki")
    p2 = Pizza(name="Tropical Delight", ingredients="Tomato Base, Cheese, Pineapple, Pilipili Hoho, Sweet Corn")


    rp1 = RestaurantPizza(price=10, pizza=p1, restaurant=r1)
    rp2 = RestaurantPizza(price=8, pizza=p2, restaurant=r1)
    rp3 = RestaurantPizza(price=12, pizza=p1, restaurant=r2)

    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()

    print("Seeding is Complete!")

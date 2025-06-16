from server.app import create_app
from server.models import db, Pizza, Restaurant, RestaurantPizza

app = create_app()

with app.app_context():
    print("Seeding pizza database...")
    
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    
    r1 = Restaurant(name="Mama Oliech's Kitchen", address="15 Rose Avenue, Nairobi")
    r2 = Restaurant(name="Nyayo Pizza Spot", address="202 Kenyatta Road, Nakuru")
    
    p1 = Pizza(name="Nyama Feast", ingredients="Tomato Sauce, Mozzarella, Beef, Sukuma Wiki")
    p2 = Pizza(name="Tropical Delight", ingredients="Tomato Base, Cheese, Pineapple, Pilipili Hoho, Sweet Corn")
    
    RestaurantPizza(price=10, pizza=p1, restaurant=r1)
    RestaurantPizza(price=8, pizza=p2, restaurant=r1)
    RestaurantPizza(price=12, pizza=p1, restaurant=r2)
    
    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()
    
    print("Seeding doneeee!")
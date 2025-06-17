# Pizza Restaurant API Documentation  

A complete backend system for managing pizza restaurants, their menus, and pizza-restaurant relationships. Built with **Flask** and **SQLAlchemy**, this API provides all the necessary endpoints for full CRUD operations.  

---  

##  Setup & Installation  

### 1. Clone and Install Dependencies  
```bash  
git clone https://github.com/yourusername/pizza-restaurant-api.git  
cd pizza-restaurant-api  
pipenv install  
pipenv shell  
```  

### 2. Configure Environment  
```bash  
echo "FLASK_APP=server.app" > .flaskenv  
echo "FLASK_DEBUG=1" >> .flaskenv  
echo "FLASK_RUN_PORT=5555" >> .flaskenv  
```  

### 3. Database Setup  
```bash  
flask db init  
flask db migrate  
flask db upgrade  
python seed.py  
```  

---  

##  API Endpoints  

### **Restaurants**  
- **GET** `/restaurants` → List all restaurants  
- **GET** `/restaurants/<int:id>` → Get restaurant details + pizzas  
- **DELETE** `/restaurants/<int:id>` → Delete a restaurant  

### **Pizzas**  
- **GET** `/pizzas` → List all available pizzas  

### **Restaurant Pizzas**  
- **POST** `/restaurant_pizzas` → Link a pizza to a restaurant  

---  

## Some example requests  

### **1. Get All Restaurants**  
```bash  
curl http://localhost:5555/restaurants  
```  
**Response:**  
```json  
[
  {
    "id": 1,
    "name": "Mama Oliech's Kitchen",
    "address": "15 Rose Avenue, Nairobi"
  }
]
```  

### **2. Get a Single Restaurant**  
```bash  
curl http://localhost:5555/restaurants/1  
```  
**Response:**  
```json  
{
  "id": 1,
  "name": "Mama Oliech's Kitchen",
  "address": "15 Rose Avenue, Nairobi",
  "pizzas": [
    {
      "id": 1,
      "name": "Nyama Feast",
      "ingredients": "Tomato Sauce, Mozzarella, Beef, Sukuma Wiki"
    }
  ]
}
```  

### **3. Link a Pizza to a Restaurant**  
```bash  
curl -X POST http://localhost:5555/restaurant_pizzas \
  -H "Content-Type: application/json" \
  -d '{"price": 15, "pizza_id": 1, "restaurant_id": 1}'  
```  
**Success (201):**  
```json  
{
  "id": 1,
  "price": 15,
  "pizza": {
    "id": 1,
    "name": "Nyama Feast",
    "ingredients": "Tomato Sauce, Mozzarella, Beef, Sukuma Wiki"
  },
  "restaurant": {
    "id": 1,
    "name": "Mama Oliech's Kitchen",
    "address": "15 Rose Avenue, Nairobi"
  }
}
```  
**Error (400):**  
```json  
{
  "errors": ["Price must be between 1 and 30"]
}
```  

---  

## 🧪 Testing with Postman  

### **1. Import the Collection**  
1. Open **Postman**  
2. Click **Import** → **Upload Files**  
3. Select the provided `pizza_api_postman_collection.json`  

### **2. Set Up Environment**  
- Create a new environment in Postman  
- Add a variable `base_url` with value `http://localhost:5555`  

### **3. Test the Endpoints**  
- **GET** `/restaurants` → Should return all restaurants  
- **POST** `/restaurant_pizzas` → Try valid and invalid prices (1-30)  
- **DELETE** `/restaurants/1` → Verify cascading deletes  

### **4. View Responses**  
- Check status codes (`200`, `201`, `400`, `404`)  
- Verify response body matches expected format  

---  

## Key Notes  
- **Price Validation**: Must be between 1 and 30  
- **Unique Constraints**:  
  - Restaurant names must be unique  
  - Pizza names must be unique  
  - A pizza can't be linked to the same restaurant twice  

---  

##  If you require some assistance...  
If the API isn't responding:  
- Ensure Flask is running (`flask run`)  
- Check port `5555` is not blocked
- Reset the database if needed (`rm instance/app.db` + re-run migrations)  



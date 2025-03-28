from pymongo import MongoClient
MONGO_URI = "mongodb+srv://flaskuser9249:9249@flask1.w9mtn.mongodb.net/?retryWrites=true&w=majority&appName=Flask1"
client = MongoClient(MONGO_URI)
db = client["sample_mflix"]  # ✅ Correct database name
collection = db["embedded_movies"]   # Collection name

# sample_users = [
#     {"username": "user1", "password": "pass123", "role": "user"},
#     {"username": "admin1", "password": "admin123", "role": "admin"}
# ]
# users_collection.insert_many(sample_users)  
users_collection = db["users"]
admins_collection = db["admins"]
canal_data_collection = db["canal_data"]
def get_users_collection():
    return users_collection
def get_admins_collection():
    return admins_collection
def get_canal_data_collection():
    return canal_data_collection
def get_subscribe_collection():
    return db["subscribe"]
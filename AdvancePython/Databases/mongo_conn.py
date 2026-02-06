# run with debug

import pymongo
import os

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

client = None

try:
    client = pymongo.MongoClient(host=host, port=int(port))
    client.admin.command("ping")
    print("--> Actual connection confirmed!")

    db = client[db_name]
    collection = db["users"]

    user_data = {"name": "John", "email": "john123@gmail.com", "age": 25}

    if not collection.find_one({"email": user_data["email"]}):
        result = collection.insert_one(user_data)
        print(f"Inserted document ID: {result.inserted_id}")
    else:
        print("User already exists in database.")

    print("\n--> Finding 'John'")
    user = collection.find_one({"name": "John"})
    print(user)

    print("\n--> Users older than 20")
    for person in collection.find({"age": {"$gt": 20}}):
        print(f"Name: {person.get('name')}, Age: {person.get('age')}")

except ConnectionError:
    print("Error: Could not connect to MongoDB. Is the service running?")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if client:
        client.close()

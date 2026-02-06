import pymongo

try:
    client = pymongo.MongoClient(
        "mongodb://localhost:27017/", serverSelectionTimeoutMS=2000
    )
    client.admin.command("ping")
    print("Actual connection confirmed!")

    db = client["my_database"]
    collection = db["users"]

    user_data = {"name": "John", "email": "john123@gmail.com", "age": 25}

    result = collection.insert_one(user_data)
    print(f"Inserted document ID: {result.inserted_id}")

    query = {"name": "John"}
    user = collection.find_one(query)
    print(user)

    for person in collection.find({"age": {"$gt": 20}}):
        print(person)

except Exception as e:
    print("Error: ", e)

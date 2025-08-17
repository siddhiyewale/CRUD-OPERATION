from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)
db = client.EmployeeDb

def update():
    try:
        name = input("\n Enter name to update: ")
        age = int(input("\n Enter new age: "))
        country = input("\n Enter new country: ")

        result = db.Employee.update_one(
            {"name": name},
            {"$set": {"age": age, "country": country}}
        )

        if result.matched_count > 0:
            print("\n Record updated successfully!\n")
        else:
            print("\n No record found with that name.\n")

    except Exception as e:
        print("Error:", str(e))

update()

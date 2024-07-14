"""
Title: insert_one_ex1.py
Author: Professor Krasso
Date: 27 June 2022
Description: Exercise 6.3
"""
# Import the MongoClient
from pymongo import MongoClient
import datetime
# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:Antfe81218@bellevueuniversity.wzejht3.mongodb.net/")
# Configure a variable to access the web335DB
db = client['web335']
# Create a new user document and added it to the users collection
new_user = {
 "firstName": "Joseph",
 "lastName": "Jones",
 "employeeId": "1014",
 "email": "j@me.com",
 "dateCreated": datetime.datetime.utcnow()
}
# Insert the document into the users collection
new_user_id = db.users.insert_one(new_user).inserted_id
print(new_user_id)
# Prove the insert worked by searching the collection for the document
print(db.users.find_one({"employeeId": "1014"}))

# Create an update query to change the user's email address
updated_user = db.users.update_one(
 {"employeeId": "1014"},
 {
 "$set": {
 "email": "joseph.jones@me.com"
 }
 }
)
print(updated_user)
# Prove the update worked by searching the collection for the user by employeeId
print(db.users.find_one({"employeeId": "1014"}))

# Build a query to remove a user document
result = db.users.delete_one({
 "employeeId": "1014"
})
# Display the results of the query
print(result)
# Prove the delete worked by searching the collection for the deleted document
print(db.users.find_one({"employeeId": "1014"}))
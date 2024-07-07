"""
Title: pymongo_conn.py
Author: Professor Krasso
Date: 27 June 2022
Desc
"""

# Import the MongoClient
from pymongo import MongoClient

import os


# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:Antfe81218@bellevueuniversity.wzejht3.mongodb.net/")
# Configure a variable to access the web335DB
db = client.web335
# Call the find function to display all of the users in the collection; use

for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
 print(user)
# Call the find_one function to display a user document by id
print(db.users.find_one({"employeeId": "1007"}))
print(db.users.find_one({"lastName": "Mozart"}))
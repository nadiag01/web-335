db.users.insertOne({"firstName": "John", "lastName": "Briggs", "employeeId": "1013", "email": "johnb@me.com"}) // Adds a new user to the user's collection with the first name john, last name briggs, employeeid 1013, and email jhonb@me// 

db.users.updateOne({"lastName": "Mozart"}, {$set: {"email": "mozart@me.com"}}) // updates Mozarts email address to mozart@me.com// 

db.users.find({}, {_id: 0, firstName: 1, lastName: 1, email: 1}) // Displays all users in the collection only showing the first name, last name , and email address// 
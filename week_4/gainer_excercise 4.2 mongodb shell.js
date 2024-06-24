db.users.find() //displays all information under user collection //

db.users.findOne({email: "jbach@me.com"}) //finds the user with the email that we passed in under user collection//

db.users.find({lastName: "Mozart"}) // finds the user with the last name that we passed in under user collection//

db.users.find({firstName: "Richard"}) //finds the user with the first name that we passed in under user collection//

db.users.find({employeeId: "1010"}) // finds the user with the employeeId that we passed in under user collection//

// displays all students withing the collection//
db.students.find()

//displays students with the first name Joe within the collection
db.student.findOne({firstName: "Joe"})

//displays updated information on one student within the collection//
db.student.updateOne({firstName: "Joe" lastName: "gainer"})

//displays deleted information on the student named Joe//
db.student.deleteOne({firstName: "Joe"})

// displays all students by house with the order houses then students//
db.houses.aggregagate([ {$lookup: {from:"students", localField: "houseId", foereignField: "houseId", as:"housedocs" }}])

//displays all students in house Gryffindor with the order Gryffindor then students//
db.houses.aggregate([ {$match: {"houseId": "h1007"}, {$lookup: {from:"students", localField: "houseId", foreignField: "houseId", as: "housedocs"}}])

//displays all students in the house with an Eagle mascot with the order house then students//
db.houses.aggregate([ {$match: {"mascot": "Eagle"}, {$lookup: {from:"students", localField: "houseId", foreignField: "houseId", as: "housedocs"}}])
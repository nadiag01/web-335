/**
 Title: WhatABook_queries.js
 Author: Leah Harris
 Date: July 17 2024
 */

 //Query to display a list of books
 db.books.find();

 //Query to display a list of books by genre
 db.books.aggregate([{$lookup: {from: 'books', localField: 'genre', foreignField: 'genre', as: 'genre_list'}}]);

 //Query to display a list of books by author
 db.books.aggregate([{$lookup: {from: 'books', localField: 'author', foreignField: 'author', as: 'author_list'}}]);

 //Query to display a book by bookId
 db.books.findOne({bookId: 'b1002'});

  

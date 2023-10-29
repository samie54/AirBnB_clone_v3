Project: AirBnB clone - MySQL

Team/Group/Collaboration Project

Date: 14/09/2023

Authors:

1. Samuel Atiemo
2. Mahmoud Khairi

Project Tasks:

0. Fork me if you can!
mandatory

1. Bug free!
mandatory
Do you remember the unittest module?

This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of the program.

2. Console improvements
mandatory
Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters:

Command syntax: create <Class name> <param 1> <param 2> <param 3>...
Param syntax: <key name>=<value>
Value syntax:
String: "<value>" => starts with a double quote
any double quote inside the value must be escaped with a backslash \
all underscores _ must be replace by spaces . Example: You want to set the string My little house to the attribute name, your command line must be name="My_little_house"
Float: <unit>.<decimal> => contains a dot .
Integer: <number> => default case
If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped
Don’t forget to add tests for this new feature!

Also, this new feature will be tested here only with FileStorage engine.

3. MySQL setup development
mandatory
Write a script that prepares a MySQL server for the project:

A database hbnb_dev_db
A new user hbnb_dev (in localhost)
The password of hbnb_dev should be set to hbnb_dev_pwd
hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

4. MySQL setup test
mandatory
Write a script that prepares a MySQL server for the project:

A database hbnb_test_db
A new user hbnb_test (in localhost)
The password of hbnb_test should be set to hbnb_test_pwd
hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail

5. Delete object
mandatory
Update FileStorage: (models/engine/file_storage.py)

Add a new public instance method: def delete(self, obj=None): to delete obj from __objects if it’s inside - if obj is equal to None, the method should not do anything
Update the prototype of def all(self) to def all(self, cls=None) - that returns the list of objects of one type of class. Example below with State - it’s an optional filtering

6. DBStorage - States and Cities
mandatory
SQLAlchemy will be your best friend!

It’s time to change your storage engine and use SQLAlchemy

7. DBStorage - User
mandatory
Update User: (models/user.py)

User inherits from BaseModel and Base (respect the order)
Add or replace in the class User:

8. DBStorage - Place
mandatory
Update Place: (models/place.py)

Place inherits from BaseModel and Base (respect the order)
Add or replace in the class Place:

9. DBStorage - Review
mandatory
Update Review: (models/review.py)

Review inherits from BaseModel and Base (respect the order)
Add or replace in the class Review:

10. DBStorage - Amenity... and BOOM!
mandatory
Update Amenity: (models/amenity.py)

Amenity inherits from BaseModel and Base (respect the order)
Add or replace in the class Amenity:



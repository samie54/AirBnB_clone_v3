Project: AirBnB clone - RESTful API

Team/Group/Collaboration Project

Date: 25/10/2023

Authors:

1. Samuel Atiemo
2. Mahmoud Khairi
3. hossam ghieth

Project Tasks:
0. Restart from scratch!
mandatory
No no no! We are already too far in the project to restart everything.

But once again, let’s work on a new codebase.

1. Never fail!
mandatory


Since the beginning we’ve been using the unittest module, but do you know why unittests are so important? Because when you add a new feature, you refactor a piece of code, etc… you want to be sure you didn’t break anything.

2. Improve storage
mandatory
Update DBStorage and FileStorage, adding two new methods. All changes should be done in the branch storage_get_count:

A method to retrieve one object:

Prototype: def get(self, cls, id):
cls: class
id: string representing the object ID
Returns the object based on the class and its ID, or None if not found

3. Status of your API
mandatory
It’s time to start your API!

Your first endpoint (route) will be to return the status of your API:

4. Some stats?
mandatory
Create an endpoint that retrieves the number of each objects by type:

In api/v1/views/index.py
Route: /api/v1/stats
You must use the newly added count() method from storage

5. Not found
mandatory
Designers are really creative when they have to design a “404 page”, a “Not found”… 34 brilliantly designed 404 error pages

Today it’s different, because you won’t use HTML and CSS, but JSON!

In api/v1/app.py, create a handler for 404 errors that returns a JSON-formatted 404 status code response. The content should be: "error": "Not found"

6. State
mandatory
Create a new view for State objects that handles all default RESTFul API actions:

In the file api/v1/views/states.py
You must use to_dict() to retrieve an object into a valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all State objects: GET /api/v1/states

Retrieves a State object: GET /api/v1/states/<state_id>

7. City
mandatory
Same as State, create a new view for City objects that handles all default RESTFul API actions:

In the file api/v1/views/cities.py
You must use to_dict() to serialize an object into valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all City objects of a State: GET /api/v1/states/<state_id>/cities

8. Amenity
mandatory
Create a new view for Amenity objects that handles all default RESTFul API actions:

In the file api/v1/views/amenities.py
You must use to_dict() to serialize an object into valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all Amenity objects: GET /api/v1/amenities

9. User
mandatory
Create a new view for User object that handles all default RESTFul API actions:

In the file api/v1/views/users.py
You must use to_dict() to retrieve an object into a valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all User objects: GET /api/v1/users

Retrieves a User object: GET /api/v1/users/<user_id>

10. Place
mandatory
Create a new view for Place objects that handles all default RESTFul API actions:

In the file api/v1/views/places.py
You must use to_dict() to retrieve an object into a valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all Place objects of a City: GET /api/v1/cities/<city_id>/places

If the city_id is not linked to any City object, raise a 404 error
Retrieves a Place object. : GET /api/v1/places/<place_id>

11. Reviews
mandatory
Create a new view for Review object that handles all default RESTFul API actions:

In the file api/v1/views/places_reviews.py
You must use to_dict() to retrieve an object into valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all Review objects of a Place: GET /api/v1/places/<place_id>/reviews

If the place_id is not linked to any Place object, raise a 404 error
Retrieves a Review object. : GET /api/v1/reviews/<review_id>

12. HTTP access control (CORS)
mandatory
A resource makes a cross-origin HTTP request when it requests a resource from a different domain, or port, than the one the first resource itself serves.

13. Place - Amenity
#advanced
Create a new view for the link between Place objects and Amenity objects that handles all default RESTFul API actions:

In the file api/v1/views/places_amenities.py
You must use to_dict() to retrieve an object into a valid JSON
Update api/v1/views/__init__.py to import this new file

14. Security improvements!
#advanced
Currently, the User object is designed to store the user password in cleartext.

It’s super bad!

To avoid that, improve the User object:

Update the method to_dict() of BaseModel to remove the password key except when it’s used by FileStorage to save data to disk. Tips: default parameters

15. Search
#advanced
For the moment, the only way to list Place objects is via GET /api/v1/cities/<city_id>/places.

Good, but not enough…

Update api/v1/views/places.py to add a new endpoint: POST /api/v1/places_search that retrieves all Place objects depending of the JSON in the body of the request.







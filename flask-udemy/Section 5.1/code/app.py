#             folder 5 : STORING RESOURCES IN DATABASE            #

'''
> Flask:This class is used to create an instance of a Flask application.
> flask_restful is an extension for Flask that simplifies the creation and more organised of REST APIs.    
> request: This object is used to handle the HTTP requests in Flask, such as getting data from a client.
> Resource: This class represents a RESTful resource, which maps to HTTP methods (GET, POST, DELETE, PUT).
> Api: This class is used to create an API object, which is used to add resources and handle routing.
> reqparse: This module is used to parse and validate incoming request data.
> JWT: This class is used to create a JSON Web Token (JWT) authentication object.
> jwt_required: This decorator is used to protect endpoints, ensuring that only authenticated users can access them.
'''
# import modules 
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from user import UserRegister
from item import Item,Itemlist        

# create app, seceret key,api call, jwt extension
app = Flask(__name__) # this is the creation of app: (Flask)
app.secret_key = "password" # sets the secret key for the application.
api = Api(app)  # api.calling  
jwt = JWT(app,authenticate,identity) # creates a new endpoint /auth for authentication.

# maps the itemlist.item,userregister 
api.add_resource(Item,"/item/<string:name>")
api.add_resource(Itemlist,"/items")
api.add_resource(UserRegister,'/register') 
if __name__ == "__main__":
    app.run(debug=True,port=3000)       
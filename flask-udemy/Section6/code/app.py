#             folder 6 : simplyifing storage  with flask-sqlalchemy            #

# video 4:
# Flask:This class is used to create an instance of a Flask application.
# request: This object is used to handle the HTTP requests in Flask, such as getting data from a client.
from flask import Flask,request
# video 4:resource,api
# Resource: This class represents a RESTful resource, which maps to HTTP methods (GET, POST, DELETE, PUT).
# Api: This class is used to create an API object, which is used to add resources and handle routing.
# video 4: reqparse
# reqparse: This module is used to parse and validate incoming request data.
from flask_restful import Resource,Api,reqparse
# video 4:JWT,jwt_required
# JWT: This class is used to create a JSON Web Token (JWT) authentication object.
# jwt_required: This decorator is used to protect endpoints, ensuring that only authenticated users can access them.
from flask_jwt import JWT,jwt_required
# video 4: module security import 
from security import authenticate,identity
# video 4:resources is a package and user is module and UserRegister is a class. 
from resources.user import UserRegister
# video 4:resources is a pakage and item is module and Item,Itemlist is a class. 
from resources.item import Item,Itemlist
# video 14:
from resources.store import Store,StoreList            

# video 4:this is the creation of app: (Flask)
app = Flask(__name__) 
# video 8:
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False 
# video 9: sqlachemy database is gonna live at the root folder of our project. # read data.db 
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqllite3:///data.db'
# video 4: This sets the secret key for the application.
app.secret_key = "password"

# video 4: this is for api.calling
api = Api(app)    
# video 10:
@app.before_first_request
def create_table(self):
    db.create_all()
# video 4: This creates a new endpoint /auth for authentication.
jwt = JWT(app,authenticate,identity) 

# video 4: maps the Item resource to the /item/<name> endpoint. 
api.add_resource(Item,"/item/<string:name>")
# video 4: Maps the ItemList resource to the /items endpoint.
api.add_resource(Itemlist,"/items")
# video 4: 
api.add_resource(UserRegister,'/register')
# video 14: 
api.add_resource(Store,"/store/<string:name>")
# video 14:
api.add_resource(StoreList,"/stores")
# video 4: app.run(port=4):
# video 4: app.run(debug=True)
if __name__ == "__main__":
# video 8: import db module with db object.   
    from db import db
# video 8:    
    db.init_app(app)
    app.run(debug=True,port=3000)       
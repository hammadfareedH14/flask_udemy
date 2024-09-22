#             folder 6 : simplyifing storage  with flask-sqlalchemy            #
'''
> Flask:This class is used to create an instance of a Flask application.
> request: This object is used to handle the HTTP requests in Flask, such as getting data from a client.
> Resource: This class represents a RESTful resource, which maps to HTTP methods (GET, POST, DELETE, PUT).
> Api: This class is used to create an API object, which is used to add resources and handle routing.
> reqparse: This module is used to parse and validate incoming request data.
> JWT: This class is used to create a JSON Web Token (JWT) authentication object.
> jwt_required: This decorator is used to protect endpoints, ensuring that only authenticated users can access them.
> Flask-SQLAlchemy: mein,aap models ko classes ke through define karte hain jo db.Model ko inherit karti hain.
'''
# module:
from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister # resources is a package and user is module and UserRegister is a class.
from resources.item import Item,Itemlist # resources is a pakage and item is module and Item,Itemlist is a class. 
from resources.store import Store,StoreList            

app = Flask(__name__) # creation of app: (Flask)
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False # disables any automatic commits(saves).
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqllite:///data.db' # sqlachemy database is gonna live at the root folder of our project.#read data.db 
app.secret_key = "password" # sets the secret key for the application.

# video 4: this is for api.calling
api = Api(app)    
# video 10:
@app.before_first_request
def create_table(self):
    db.create_all()

jwt = JWT(app,authenticate,identity) 

# maps the endpoints 
api.add_resource(Item,"/item/<string:name>")
api.add_resource(Itemlist,"/items")
api.add_resource(UserRegister,'/register')
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")

if __name__ == "__main__":
    from db import db # module
    db.init_app(app)
    app.run(debug=True,port=3000)       
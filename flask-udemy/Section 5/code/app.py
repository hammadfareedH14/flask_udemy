#             folder 5 : STORING RESOURCES IN DATABASE            #

# video 2:
# Flask:This class is used to create an instance of a Flask application.
# request: This object is used to handle the HTTP requests in Flask, such as getting data from a client.
from flask import Flask,request
# video 2:resource,api
# Resource: This class represents a RESTful resource, which maps to HTTP methods (GET, POST, DELETE, PUT).
# Api: This class is used to create an API object, which is used to add resources and handle routing.
# video 2: reqparse
# reqparse: This module is used to parse and validate incoming request data.
from flask_restful import Resource,Api,reqparse
# video 2:JWT,jwt_required
# JWT: This class is used to create a JSON Web Token (JWT) authentication object.
# jwt_required: This decorator is used to protect endpoints, ensuring that only authenticated users can access them.
from flask_jwt import JWT,jwt_required
# video 2: modeule security import 
from security import authenticate,identity
# video 6:
from user import UserRegister
# video 8:
from item import Item,Itemlist        

# video 2:this is the creation of app: (Flask)
app = Flask(__name__) 

# video 2: This sets the secret key for the application.
app.secret_key = "password"

# video 2: this is for api.calling
api = Api(app)    

# video 2: This creates a new endpoint /auth for authentication.
jwt = JWT(app,authenticate,identity) 

# video 2:This list will store all the items.
# items = [] 

# video 2: create class Item         
# class Item(Resource):
# video 2: This initializes the parser.    
#     parser =reqparse.RequestParser()
# video 2:    
#     parser.add_argument(
        # 'price',
        # type=float,
        # required=True,
        # help='This field cannot be left blank!'  # Ensures the 'price' field is not empty.
        # ) 
# this method get the data from client-sdide we just want to show it and store in {} server-side 
# video 2: jwt_required(is decorator) mean authenticate before call a get method.
#     @jwt_required()

# video 2:    
#     def get(self,name):
# video 2: method 1: Retrieves the item by name.
        # item = next(filter(lambda x:x["name"]==name, items),None)
# video 2: method 2: return list
        # item = list(filter(lambda x:x["name"]==name, items),None)  
        
# video 2:   returns the item if found, else returns 404.
        # return {"items":item},200 if item else 404

# video 2: iterator
        # for item in items:

# video 2 match name
        #     if item["name"] == name:

# video 2: return item
              # return item                        

# video 2:
        #         return {"item":None},404    #item not found in get method 404!      
    
    # the post method used for send data to client-side which we create new-one and store in some  {} ---> json 
# video 2:    
#     def post(self,name):
# video 2:
        # parser =reqparse.RequestParser()        
# video 2:
        # parser.add_argument('price',
        #         type=float,
        #         required=True
        #         help='this feild cannot be left blank!.'
        # ) 
# video 2: method 1: self method        
        # data = parser.parse_args()               
            
# video 2:
        # if next(filter(lambda x:x["name"] == name,items),None):

# video 2:
        #     return {"message":"An item with name '{}' already exists.".format(name)},400
        
# video 2: method 2: class method # Parses the request data.
        # data = Item.parser.parse_args()   
# video 2: method 1: 
        # data = request.get_json()

# video 2: method 2: mean no requierd content typed header only required content.
        # data = request.get_json(force=True)

# video 2: method 2: basically return None. 
        # data = request.get_json(force=True)
# video 2:
#       item = {"name":name,"price":12.00}     
# video 2:   Creates a new item.  
        # item = {"name":name,"price":data["price"]}
# video 2: Adds the item to the list. 
        # items.append(item)
# video 2: Returns the newly created item with status code 201.        
        # return item,201

# video 2:    
#     def delete(self,name):
# video 2: 
        # global items
# video 2:  Deletes the item by name.      
        # items = list(filter(lambda x: x["name"] != name,items))
# video 2:
        # return {"message": "Item Deleted"}
# video 2:
#     def put(self,name):
# video 2: 
        # parser =reqparse.RequestParser()
# video 2:        
        # parser.add_argument('price',
        #         type=float,
        #         required=True
        #         help='this feild cannot be left blank!.'
        # )   
# video 2: method 2: class method # Parses the request data.
        # data = Item.parser.parse_args()            
# video 2: self method
        # data = parser.parse_args()              
# video 2:
        # data = request.get_json()

# video 2  Retrieves the item by name.
        # item = next(filter(lambda x:x["name"] == name,items),None)
# video 2:        
        # if item is None:
# video 2: Creates a new item if not found.           
        #     item = {"name":name,"price":data["price"]}

# video 2: ds the item to the list.
        #     items.append(item)
        # else:
# video 2    Updates the existing item.        
        #     item.update(data)
# video 2:   return item         
        # return item

# video 2: create a class Itemlist
# class Itemlist(Resource):

# all itemlist stored in the items = [ ] which i created before classes (resources):
# video 2: create a method name get
#     def get(self):

#  video 2:   turns all items with status code 200.        
        # return {"items":items}, 200  # 200 error for successful retrievel data

# video 2: maps the Item resource to the /item/<name> endpoint. 
api.add_resource(Item,"/item/<string:name>")

# video 2: Maps the ItemList resource to the /items endpoint.
api.add_resource(Itemlist,"/items")
# video 6: 
api.add_resource(UserRegister,'/register') 
# video 2 app.run(port=4):
# video 2: app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True,port=3000)       
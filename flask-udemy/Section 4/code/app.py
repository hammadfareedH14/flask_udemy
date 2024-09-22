#             folder 4 : FLASK restful more efiicent devolpment            #

# video 4:
# Flask:This class is used to create an instance of a Flask application.
# request: This object is used to handle the HTTP requests in Flask, such as getting data from a client.
from flask import Flask,request
# video 4:resource,api
# Resource: This class represents a RESTful resource, which maps to HTTP methods (GET, POST, DELETE, PUT).
# Api: This class is used to create an API object, which is used to add resources and handle routing.
# video 13: reqparse
# reqparse: This module is used to parse and validate incoming request data.
from flask_restful import Resource,Api,reqparse
# video 10:JWT,jwt_required
# JWT: This class is used to create a JSON Web Token (JWT) authentication object.
# jwt_required: This decorator is used to protect endpoints, ensuring that only authenticated users can access them.
from flask_jwt import JWT,jwt_required
# video 10: modeule security import 
from security import authenticate,identity

# video 4:this is the creation of app: (Flask)
app = Flask(__name__) 

# video 9: This sets the secret key for the application.
app.secret_key = "password"

# video 4: this is for api.calling
api = Api(app)    

# video 10: This creates a new endpoint /auth for authentication.
jwt = JWT(app,authenticate,identity) 

# video 6:This list will store all the items.
items = [] 

# video 4 create a class student
class Student(Resource):
# video 4:  create method name get  
    def get(self,name):
# video 4: Returns the student's name.       
        return {'student':name}
# video 6: create class Item         
class Item(Resource):
# video 14: This initializes the parser.    
    parser =reqparse.RequestParser()
# video 14:    
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This field cannot be left blank!'  # Ensures the 'price' field is not empty.
        ) 
# this method get the data from client-sdide we just want to show it and store in {} server-side 
# video 10: jwt_required(is decorator) mean authenticate before call a get method.
    @jwt_required()

# video 6:    
    def get(self,name):

# video 8: method 1: Retrieves the item by name.
        item = next(filter(lambda x:x["name"]==name, items),None)
# video 8: method 2: return list
        # item = list(filter(lambda x:x["name"]==name, items),None)  
        
# video 8:   returns the item if found, else returns 404.
        return {"items":item},200 if item else 404

# video 6: iterator
        # for item in items:

# video 6 match name
        #     if item["name"] == name:

# video 6: return item
              # return item                        

# video 6:
        #         return {"item":None},404    #item not found in get method 404!      
    
    # the post method used for send data to client-side which we create new-one and store in some  {} ---> json 
# video 6:    
    def post(self,name):
# video 14:
        # parser =reqparse.RequestParser()        
# video 14:
        # parser.add_argument('price',
        #         type=float,
        #         required=True
        #         help='this feild cannot be left blank!.'
        # ) 
# video 14: method 1: self method        
        # data = parser.parse_args()               
            
# video 8:
        if next(filter(lambda x:x["name"] == name,items),None):

# video 8:
            return {"message":"An item with name '{}' already exists.".format(name)},400
        
# video 14: method 2: class method # Parses the request data.
        data = Item.parser.parse_args()   
# video 7: method 1: 
        # data = request.get_json()

# video 7: method 2: mean no requierd content typed header only required content.
        # data = request.get_json(force=True)

# video 7: method 2: basically return None. 
        # data = request.get_json(force=True)

# video 6:
#       item = {"name":name,"price":12.00}     

# video 6:   Creates a new item.  
        item = {"name":name,"price":data["price"]}

# video 6: Adds the item to the list. 
        items.append(item)

# video 6: Returns the newly created item with status code 201.        
        return item,201

# video 11:    
    def delete(self,name):

# video 11: 
        global items

# video 11:  Deletes the item by name.      
        items = list(filter(lambda x: x["name"] != name,items))

# video 11:
        return {"message": "Item Deleted"}
    
# video 12:
    def put(self,name):
# video 13: 
        # parser =reqparse.RequestParser()
# video 13:        
        # parser.add_argument('price',
        #         type=float,
        #         required=True
        #         help='this feild cannot be left blank!.'
        # )   
# video 14: method 2: class method # Parses the request data.
        data = Item.parser.parse_args()            
# video 13: self method
        # data = parser.parse_args()              
# video 12:
        # data = request.get_json()

# video 12  Retrieves the item by name.
        item = next(filter(lambda x:x["name"] == name,items),None)
# video 12:        
        if item is None:
# video 12: Creates a new item if not found.           
            item = {"name":name,"price":data["price"]}

# video 12: ds the item to the list.
            items.append(item)
        else:
            
# video 12    Updates the existing item.        
            item.update(data)
# video 12:   return item         
        return item

# video 7: create a class Itemlist
class Itemlist(Resource):

# all itemlist stored in the items = [ ] which i created before classes (resources):
# video 7: create a method name get
    def get(self):

#  video 7:   turns all items with status code 200.        
        return {"items":items}, 200  #200 error for successful retrievel data

# video 4: aps the Student resource to the /student/<name> endpoint.   
api.add_resource(Student,"/student/<string name>")

# video 6: maps the Item resource to the /item/<name> endpoint. 
api.add_resource(Item,"/item/<string:name>")

# video 7: Maps the ItemList resource to the /items endpoint.
api.add_resource(Itemlist,"/items")

# video 4 app.run(port=4):
# video 7: app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True,port=3000)       
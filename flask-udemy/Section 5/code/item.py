# video 8:
import sqlite3
# video 8:
from flask_restful import Resource,reqparse
# video 8:
from flask_jwt import jwt_required

class Item(Resource):
# video 8: This initializes the parser.    
    parser =reqparse.RequestParser()
# video 8:    
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This field cannot be left blank!'  # Ensures the 'price' field is not empty.
        ) 
# this method get the data from client-sdide we just want to show it and store in {} server-side 
# video 2: jwt_required(is decorator) mean authenticate before call a get method.
    @jwt_required()

# video 8: create a method name get.   
    def get(self,name):
# video 9: find_by_name method call in item variable   
        item = self.find_by_name(name)
# video 9: check item exists
        if item:
# video 9: return item 
            return item
# video 9: otherwise return 'message item not found'        
        return {'message':'Item not found'},404  
    
# video 9:class method use
    @classmethod 
# video 9: create a method name find_by_name        
    def find_by_name(cls,name):
# video 9: establish a connection to database        
        connection = sqlite3.connect('data.db')
# video 9: get a cursor       
        cursor = connection.cursor()
# video 9: slect item       
        query = "SELECT * FROM item WHERE name=?"
# video 9: run query       
        result =cursor.execute(query,(name,))
# video 9: fetch a row       
        row = result.fetchone()
# video 9: close a connection       
        connection.close()
# video 9: check row exists       
        if row:
# video 9: return item           
            return{'item':{'name':row[0],'price':row[1]}}
           
# the post method used for send data to client-side which we create new-one and store in some  {} ---> json 
# video 2: create a method post    
    def post(self,name):
# video 9: method 2:check item name is already exists using find_by_name_ method.
        # if Item.find_by_name(name):
# video 9: method 2:check item name is already exists using find_by_name_ method.
        if self.find_by_name(name):
# video 9: return message.
            return {"message":"An item with name '{}' already exists.".format(name)},400
# video 2: Parses the request data.
        data = Item.parser.parse_args()      
# video 9: Creates a new item.  
        item = {"name":name,"price":data["price"]}    
# video 11: try and execept block used.
        try:
           self.insert(item)                
        except:
            return {'message':'An error accured inserting the item.'},500
# video 11:  return item sucessfully.       
        return item,201 
# video 11:
    @classmethod 
    def insert(cls,item):
# video 11: establish a connection to database        
        connection = sqlite3.connect('data.db')
# video 11: get a cursor       
        cursor = connection.cursor()
# video 11: insert a new row in item table.
        query = "INSERT INTO items VALUES (?,?)"
# video 11: run query  and   subsitute parameter   
        cursor.execute(query,(item['name'],item['price']))
# video 11: save changes in database
        connection.commit()        
# video 11: close a connection       
        connection.close()

# video 10: create a method delete    
    def delete(self,name):
# video 10: establish a connection to database        
        connection = sqlite3.connect('data.db')
# video 10: get a cursor       
        cursor = connection.cursor()
# video 10: delte a new row in item table.
        query = "DELETE FROM items WHERE names=?"
# video 10: run query  and  specific name  
        cursor.execute(query,(name,))
# video 10: save changes in database
        connection.commit()        
# video 10: close a connection       
        connection.close()
## video 10: retrun message.
        return {'messsage':'Item deleted'}

# video 8: create a method put    
    def put(self,name): 
# video 12: # Parses the request data.
        data = Item.parser.parse_args()            
# video 12:  Retrieves the item by name.
        item = self.find_by_name(name)
        updated_item = {"name":name,"price":data["price"]}      
# video 12:        
        if item is None:
# video 12: inserts the exsisting item .
           try: 
                self.insert(updated_item)
           except:
                return {'message':'An error accured inserting the item'},500    
# video 12    Updates the existing item.              
        else:
          try:    
             self.update(updated_item)
          except:
                return {'message':'An error accured updating the item'},500    
                  
# video 12:
        return updated_item

# video 12:
    @classmethod 
    def insert(cls,item):
# video 11: establish a connection to database        
        connection = sqlite3.connect('data.db')
# video 11: get a cursor       
        cursor = connection.cursor()
# video 11: insert a new row in item table.
        query = "UPDATE items SET price=? WHERE name=?"
# video 11: run query  and   subsitute parameter   
        cursor.execute(query,(item['name'],item['price']))
# video 11: save changes in database
        connection.commit()        
# video 11: close a connection       
        connection.close()

# video 2: create a class Itemlist
class Itemlist(Resource):

# all itemlist stored in the items = [ ] which i created before classes (resources):
# video 2: create a method name get
    def get(self):
# video 13: establish a connection to database        
        connection = sqlite3.connect('data.db')
# video 13: get a cursor       
        cursor = connection.cursor()
# video 13: insert a new row in item table.
        query = "SELECT * FROM items"
# video 13: run query  and   subsitute parameter   
        result = cursor.execute(query)
# video 13:
        items=[]
# video 13:
        for row in result:
            items.append({'name':row[0],'price':row[1]})                            
# video 13: close a connection       
        connection.close()

#  video 13:   turns all items with status code 200.        
        return {"items":items}, 200  #200 error for successful retrievel data
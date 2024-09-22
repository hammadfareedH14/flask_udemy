# module:
import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser =reqparse.RequestParser() 
    parser.add_argument(
        'price', # name of argumenet
        type=float, # type is float othetrwise throw error.
        required=True, # argument is mandatory otherwise throw error.
        help='This field cannot be left blank!'  # Ensures the 'price' field is not empty.
        )
     
    @jwt_required() 
    def get(self,name):
        item = self.find_by_name(name) 
        if item: 
            return item     
        return {'message':'Item not found'},404 
    
    @classmethod # class method 
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db') # estabilish a connection with sqlite database
        cursor = connection.cursor() # create a cursor object to interact with database
        query = "SELECT * FROM item WHERE name=?" # select all coulumn in items table where name matched 
        result =cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        if row: 
            return{'item':{'name':row[0],'price':row[1]}} # return row 
        return {'message':'item not found.'}   
    def post(self,name):
      # if Item.find_by_name(name): # method 1: class method. # 
        if self.find_by_name(name): # method 2: self method.
            return {"message":"An item with name '{}' already exists.".format(name)},400
        data = Item.parser.parse_args()      
        item = {"name":name,"price":data["price"]}    
        try:
           self.insert(item)                
        except:
            return {'message':'An error accured inserting the item.'},500
        return item,201 
    
    @classmethod 
    def insert(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query,(item['name'],item['price']))
        connection.commit()        
        connection.close()

    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE names=?"
        cursor.execute(query,(name,))
        connection.commit()        
        connection.close()
        return {'messsage':'Item deleted'}

    def put(self,name): 
        data = Item.parser.parse_args()            
        item = self.find_by_name(name) # Retrieves the item by name.
        updated_item = {"name":name,"price":data["price"]}      
        if item is None:
           try: 
                self.insert(updated_item)
           except:
                return {'message':'An error accured inserting the item'},500    
        else:
          try:    
             self.update(updated_item)
          except:
                return {'message':'An error accured updating the item'},500    
        return updated_item

    @classmethod 
    def insert(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,(item['name'],item['price']))  # run query and subsitute parameter 
        connection.commit()        
        connection.close()

class Itemlist(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items" 
        result = cursor.execute(query)
        items=[]
        for row in result:
            items.append({'name':row[0],'price':row[1]})                            
        connection.close()
        return {"items":items}, 200  #200 error for successful retrievel data
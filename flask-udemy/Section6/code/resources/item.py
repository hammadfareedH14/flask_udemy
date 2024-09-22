# video 5:
# import sqlite3
# video 5:
from flask_restful import Resource,reqparse
# video 5:
from flask_jwt import jwt_required
# video 5:
from models.item import ItemModel

class Item(Resource):
# video 5: This initializes the parser.    
    parser =reqparse.RequestParser()
# video 5:    
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This field cannot be left blank!'  # Ensures the 'price' field is not empty.
        ) 
    parser.add_argument(
        'store_id',
        type=float,
        required=True,
        help='every item need  a store id.'  # Ensures the 'price' field is not empty.
        ) 
# this method get the data from client-sdide we just want to show it and store in {} server-side 
# video 5: jwt_required(is decorator) mean authenticate before call a get method.
# video 5: create a method name get.
    @jwt_required()   
    def get(self,name):
# video 5: find_by_name method call in item variable   
        item = ItemModel.find_by_name(name)
# video 9: check item exists
        if item:
# video 5: method 1: return item dictonary  
        #     return item
# video 5: method 2: return item object
                return item.json()        
# video 5: otherwise return 'message item not found'        
        return {'message':'Item not found'},404  
    

           
# the post method used for send data to client-side which we create new-one and store in some  {} ---> json 
# video 5: create a method post    
    def post(self,name):
# video 9: method 2:check item name is already exists using class item .
        # if Item.find_by_name(name):
# video 9: method 2:check item name is already exists using itemmodel class.
        if ItemModel.find_by_name(name):
# video 5: return message.
            return {"message":"An item with name '{}' already exists.".format(name)},400
# video 5: Parses the request data.
        data = Item.parser.parse_args()      
# video 9: method 1:Creates a new item # dictonary.  
        # item = {"name":name,"price":data["price"]}
# video 9: method 2:Creates a new item # itemmodel object.  
        item = ItemModel(name,data['price'],data['store_id'])
# video 5: try and execept block used.
        try:
# video 5:method 1: use item variable method 1(dictonary)           
        #    ItemModel.insert(item)   
# video 5: method 2: use item  method 2:(itemmodel object)
             item.save_to_db()   
        except:
            return {'message':'An error accured inserting the item.'},500
# video 5:  return item sucessfully.       
        return item.json(),201 

# video 5: create a method delete    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_to_db()
        return {'messsage':'Item deleted'} 
# video 5: establish a connection to database        
        # connection = sqlite3.connect('data.db')
# video 5: get a cursor       
        # cursor = connection.cursor()
# video 5: delte a new row in item table.
        # query = "DELETE FROM items WHERE names=?"
# video 5: run query  and  specific name  
        # cursor.execute(query,(name,))
# video 5: save changes in database
        # connection.commit()        
# video 5: close a connection       
        # connection.close()
## video 5: retrun message.
        # return {'messsage':'Item deleted'}

# video 5: create a method put    
    def put(self,name): 
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
        #     item=ItemModel(name,data['price'],data['store_id'])
            item=ItemModel(name,**data)
              
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()        
# video 5: # Parses the request data.
        # data = Item.parser.parse_args()            
# video 5:  Retrieves the item by name.
        # item = ItemModel.find_by_name(name)
# video 5: method 1:Creates a new item # dictonary.  
        # updated_item = {"name":name,"price":data["price"]} 
# video 5: method 1:Creates a new item # dictonary.  
        # updated_item = ItemModel(name,data['price'])
# video 5:        
        # if item is None:
# video 12: inserts the exsisting item .
        #    try: 
# video 5:method 1: use updated_item variable method 1(dictonary)           
                # ItemModel.insert(updated_item)
# video 5:method 2: use updated_item variable method 2 (itemmodel object)     
                # updated_item.insert()
        #    except:
                # return {'message':'An error accured inserting the item'},500    
# video 5    Updates the existing item.              
        # else:
        #   try: 
# video 5:method 1: use updated_item variable method 1(dictonary)                           
#            ItemModel.update(updated_item)
# video 5:method 2: use updated_item variable method 2 (itemmodel object)     
        #      updated_item.update()
        #   except:
                # return {'message':'An error accured updating the item'},500    
                  
# video 5: method 1: return item object
        # return updated_item.json
# video 5: method 2: return item in dictonary  
        # return updated_item.json()

# video 4: create a class Itemlist
class Itemlist(Resource):

# all itemlist stored in the items = [ ] which i created before classes (resources):
# video 4: create a method name get
    def get(self):
# video 10: method 1: list comphrension
        return {"items":[item.json()for item in ItemModel.query.all()]}
# video 10: method 1: list comphrension
        # return {"items":list(map(lambda x:x.json(),ItemModel.query.all()))}
        
# video 13: establish a connection to database        
        # connection = sqlite3.connect('data.db')
# video 13: get a cursor       
        # cursor = connection.cursor()
# video 13: insert a new row in item table.
        # query = "SELECT * FROM items"
# video 13: run query  and   subsitute parameter   
        # result = cursor.execute(query)
# video 13:
        # items=[]
# video 13:
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})                            
# video 13: close a connection       
        # connection.close()

#  video 13:   turns all items with status code 200.        
        # return {"items":items}, 200  #200 error for successful retrievel data
    
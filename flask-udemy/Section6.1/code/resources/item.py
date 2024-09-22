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
        help='every item need  a store id.' 
        ) 

    @jwt_required()   
    def get(self,name):
# video 5: find_by_name method call in item variable   
        item = ItemModel.find_by_name(name) # find_by_name method call in item variable 
        if item:
        #     return item # method 1: return item dictonary 
              return item.json() # method 2: return item object      
        return {'message':'Item not found'},404  
    
    def post(self,name):
      # if Item.find_by_name(name): # method 1:check item name is already exists using class item.
        if ItemModel.find_by_name(name): # method 2:check item name is already exists using itemmodel class.
            return {"message":"An item with name '{}' already exists.".format(name)},400
        data = Item.parser.parse_args() # parsed the argumnet.     
        # item = {"name":name,"price":data["price"]}  # method 1:Creates a new item using dictonary.  
        item = ItemModel(name,data['price'],data['store_id']) # method 2: Create a new item using itemmodel object.  
        try:
        #    ItemModel.insert(item)   
             item.save_to_db()   
        except:
            return {'message':'An error accured inserting the item.'},500
        return item.json(),201 

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_to_db()
        return {'messsage':'Item deleted'} 
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "DELETE FROM items WHERE names=?"
        # cursor.execute(query,(name,))
        # connection.commit()        
        # connection.close()
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
        # data = Item.parser.parse_args()  # parse the argument          
        # item = ItemModel.find_by_name(name) 
        # updated_item = {"name":name,"price":data["price"]} # method 1:
        # updated_item = ItemModel(name,data['price']) # method 2:
        # if item is None:
        #    try: 
                # ItemModel.insert(updated_item) # method 1: use updated_item variable method 1(dictonary)    
                # updated_item.insert() # method 2 use updated_item variable (itemmodel object)    
        #    except:
        #           return {'message':'An error accured inserting the item'},500    
        # else:
        #   try:                         
#            ItemModel.update(updated_item)
        #      updated_item.update()
        #   except:
                # return {'message':'An error accured updating the item'},500                      
        # return updated_item.json()

class Itemlist(Resource):
    def get(self):
        return {"items":[item.json()for item in ItemModel.query.all()]} # method 1: list comphrension 
        # return {"items":list(map(lambda x:x.json(),ItemModel.query.all()))} # method 2: mapp with lamda 
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items=[]
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})                            
        # connection.close()
        # return {"items":items}, 200  # 200 error for successful retrievel data
    
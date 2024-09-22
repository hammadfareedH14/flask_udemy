
# video 14:
from flask_restful import Resource
# video 14:
from models.store import StoreModel

# video 14:
class Store(Resource):
    def get(self,name):
        Store = StoreModel.find_by_name(name)
        if Store:
                return Store.json()              
        return {'message':'store not found'},404
# video 14:    
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message":"An item with name '{}' already exists.".format(name)},400
        Store = StoreModel(name)        
        try:
            Store.save_to_db()   
        except:
            return {'message':'An error accured while creating the store.'},500
        return Store.json(),201 
# video 14:
    def delete(self,name):
        Store = StoreModel.find_by_name(name)
        if Store:
                return Store.delete_to_db()              
        return {'message':'store deleted'},404


# video 14:
class StoreList(Resource):
    def get(self):
# video 14: method 1: list comphrension
        return {"stores":[item.json()for item in StoreModel.query.all()]}
# video 14: method 2: list comphrension
        # return {"stores":list(map(lambda x:x.json(),ItemModel.query.all()))}
             
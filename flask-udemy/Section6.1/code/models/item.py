# video 5:
import sqlite3
# video 8:
from db import db

class ItemModel(db.Model): # Flask-SQLAlchemy mein,aap models ko classes ke through define karte hain jo db.Model ko inherit karti hain.
    __tablename__ = 'items' # __tablename__ attribute ko use karke hum specify karte hain ki ye class kis table ko represent karegi. 
    '''
    db.Column ko data type aur optional parameters jese primary_key=True pass karna hota hai.
    '''

    id = db.Column(db.Integer, primary_key=True) # id, name, aur price ko db.Column method ke through define karte hain. 
    name = db.Column(db.String(80)) # db.Column ko data type aur optional parameters jese primary_key=True pass kara hai.
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')   

    def __init__(self,name,price,store_id): # constructor
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self): # return json
        return {'name':self.name,'price':self.price} 
        
    @classmethod       
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() # method 2:code after video 9
     
        # connection = sqlite3.connect('data.db') # method 1: code before video 9.
        # cursor = connection.cursor()
        # query = "SELECT * FROM item WHERE name=?"
        # result =cursor.execute(query,(name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return{'item':{'name':row[0],'price':row[1]}} # method 1: self method
        #     return cls(row[0],row[1]) # method 2 cls method      
        #     return cls(*row) # method 3: cls unpack method.  

#     def insert(cls,item) # method 1: class method
#     def insert(self): # method 2:self method #  method useful for both update and insert.
    def save_to_db(self):         
        db.session.add(self)
        db.session.commit()
      #  connection = sqlite3.connect('data.db')
      #  cursor = connection.cursor()
      #  query = "INSERT INTO items VALUES (?,?)"
      # cursor.execute(query,(item['name'],item['price']))
      # cursor.execute(query,(self.name,self.item))     
      # connection.commit()        
      # connection.close()
     
    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
       # @classmethod
       # def update(cls,item): 
       # connection = sqlite3.connect('data.db')
       # cursor = connection.cursor()
       # query = "UPDATE items SET price=? WHERE name=?"
       # cursor.execute(query,(self.name,self.item))
       # cursor.execute(query,(item['name'],item['price']))        
       # connection.commit()        
       # connection.close()
    
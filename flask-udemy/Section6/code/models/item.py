# video 5:
# import sqlite3
# video 8:
from db import db

# video 8: Flask-SQLAlchemy mein, aap models ko classes ke through define karte hain jo db.Model ko inherit karti hain.
class ItemModel(db.Model):
    # video 8: __tablename__ attribute ko use karke hum specify karte hain ki ye class kis table ko represent karegi.  
    __tablename__ = 'items'
    '''
    video 8: id, name, aur price ko db.Column method ke through define karte hain. 
    db.Column ko data type aur optional parameters jese primary_key=True pass karna hota hai.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
# video 13:    
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
# video 13:
    store = db.relationship('StoreModel')   
# video 5: constructor    
    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
# video 5: return json        
    def json(self):
        return {'name':self.name,'price':self.price} 
        
# video 5: # code before video 9 #class method use and create a method find_by_name.
# The find_by_name method is a class method that allows you to search for a record in the database by its name field. 
# It uses the @classmethod decorator to indicate that it operates on the class itself rather than on an instance. 
# The method takes two parameters: cls, representing the class, and name, the value to search for. 
# It performs a query on the class's associated database table, 
# filtering for records where the name matches the provided value, 
# and returns the first matching record or None if no match is found.

    @classmethod       
    def find_by_name(cls,name):
# video 9: code after video 9:
        return cls.query.filter_by(name=name).first()
# video 5: establish a connection to database        
        # connection = sqlite3.connect('data.db')
# video 5: get a cursor       
        # cursor = connection.cursor()
# video 5: slect item       
        # query = "SELECT * FROM item WHERE name=?"
# video 5: run query       
        # result =cursor.execute(query,(name,))
# video 5: fetch a row # The fetchone method returns the next row of a query result set or None in case there is no row left.       
        # row = result.fetchone()
# video 5: close a connection       
        # connection.close()
# video 5: check row exists       
        # if row:
# video 5: method 1: return item  # dictonary         
        #     return{'item':{'name':row[0],'price':row[1]}}
# video 5: method 2: return item  # cls object.        
        #       return cls(row[0],row[1])       
# video 5: method 3: return item  # argumnet unpacking method.        
        #       return cls(*row)  

# video 5:method 1:class method 
# @ classmethod
# def insert(cls,item)
# video 5:method 2:self method 
# method useful for both update and insert.
#     def insert(self):
# video 9:
    def save_to_db(self):         
        db.session.add(self)
        db.session.commit()
# video 5: establish a connection to database        
        # connection = sqlite3.connect('data.db')
# video 5: get a cursor       
        # cursor = connection.cursor()
# video 5: insert a new row in item table.
        # query = "INSERT INTO items VALUES (?,?)"
# video 5: method 1: class method perform this action
        # cursor.execute(query,(item['name'],item['price']))
# video 5: method 2: self methodmethod perform this action  
        # cursor.execute(query,(self.name,self.item))
     
# video 5: save changes in database
        # connection.commit()        
# video 5: close a connection       
        # connection.close()

# video 1:method 1: cls method update
#     @classmethod
#     def update(cls,item):
# video 1:method 2: self method update
    
    def delte_to_db(self):
        db.session.delete(self)
        db.session.commit()
# video 5: establish a connection to database        
        # connection = sqlite3.connect('data.db')
# video 5: get a cursor       
        # cursor = connection.cursor()
# video 5: insert a new row in item table.
        # query = "UPDATE items SET price=? WHERE name=?"
# video 5: method 1: self method perform this action
        # cursor.execute(query,(self.name,self.item))
# video 5: method 2: class method perform this action
#       cursor.execute(query,(item['name'],item['price']))        

# video 5: save changes in database
        # connection.commit()        
# video 5: close a connection       
        # connection.close()
    
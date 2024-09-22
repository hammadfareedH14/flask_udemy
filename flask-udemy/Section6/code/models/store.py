# video 5:
# import sqlite3
# video 8:
from db import db

# video 8: Flask-SQLAlchemy mein, aap models ko classes ke through define karte hain jo db.Model ko inherit karti hain.
class StoreModel(db.Model):
    # video 8: __tablename__ attribute ko use karke hum specify karte hain ki ye class kis table ko represent karegi.  
    __tablename__ = 'stores'
    '''
    video 8: id, name, aur price ko db.Column method ke through define karte hain. 
    db.Column ko data type aur optional parameters jese primary_key=True pass karna hota hai.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
# video 13: lazy = dynamic: items are not loaded until they are explicitly requested. 
    items = db.relationship('ItemModel',lazy = 'dynamic')    
# video 5: constructor    
    def __init__(self,name):
        self.name = name
# video 13: return json        
    def json(self):
        return {'name':self.name,'items':[item.json()for item in self.items.all()]} 
        
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
# video 9:
    def save_to_db(self):         
        db.session.add(self)
        db.session.commit()
        
    def delte_to_db(self):
        db.session.delete(self)
        db.session.commit()
    


# video 5:
import sqlite3
from db import db
class UserModel(db.model):
# class User(db.Model):
    __tablename__ = 'users'  # Correctly define the table name
# video 8:
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(80))  
    password = db.Column(db.String(80)) 

    def __init__(self,username,password):
# video 5        
        # self.id = _id
# video 5        
        self.username = username
# video 5:        
        self.password = password 

# video 10:
    def save_to_db(self):
           db.session.add(self)  # Add the instance to the session
           db.session.commit()  # Commit the session to save the instance to the database
# video 5: method 1: define function name 
    # def find_by_username(self,username):
# video 5: method 2: define function name   
    @classmethod  
    def find_by_username(cls,username):
# video 10:       
       return cls.query.filter_by(username=username).first()
          
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        # query = "SELECT * FROM  users WHERE username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row:
            # User = User(row[0],row[1],row[2]) # method 1: match all user attribute(id,name,password)
            # User = cls(row[0],row[1],row[2]) # :method 2: match all user attribute(id,name,password)
        #      return cls(*row) # method 3: match all user attribute(id,name,password)
        # else:
        #     User = None
        # connection.close()
        # return User  
            
    # def find_by_username(self,username): # self method.
    @classmethod    
    def find_by_id(cls,_id): # cls method
       return cls.query.filter_by(id=_id).first()
        # Connection = sqlite3.connect("data.db")
        # cursor = Connection.cursor()
        # query = "SELECT * FROM  users WHERE id=?"
        # result = cursor.execute(query,(_id,))
        # row = result.fetchone()
        # if row:
            # User = User(row[0],row[1],row[2])
            # User = cls(row[0],row[1],row[2])
        #     return cls(*row)
        # else:
        #     User = None
        # Connection.close()
        # return User            
    
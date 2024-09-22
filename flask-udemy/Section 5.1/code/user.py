
# modue:
import sqlite3
from flask_restful import Resource,reqparse

class User: # constructor
    def __init__(self,_id,username,password): # constructor
        self.id = _id
        self.username = username
        self.password = password 

    @classmethod  
    def find_by_username(cls,username): # class method 
        connection = sqlite3.connect("data.db") 
        cursor = connection.cursor()
        query = "SELECT * FROM  users WHERE username=?" # Queries the users table to retrieves all columns,Filters rows where username matches the provided value.
        result = cursor.execute(query,(username,))
        row = result.fetchone()
# video 5:        
        if row:
            # User = User(row[0],row[1],row[2]) # method 1: match all user attribute(id,name,password)
            # User = cls(row[0],row[1],row[2]) # method 2: match all user attribute(id,name,password)
             return cls(*row) # method 3: match all user attribute(id,name,password)
        else:      
            User = None
        connection.close()
        return User  
            
    # def find_by_username(self,username): # method 1: self method
    @classmethod
    def find_by_id(cls,_id): # method 2: class method
        Connection = sqlite3.connect("data.db") 
        cursor = Connection.cursor()
        query = "SELECT * FROM  users WHERE id=?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        if row:
            return cls(*row)
        else:
            User = None
        Connection.close()
        return User            

class UserRegister(Resource): # create a class user register.   
        parser =reqparse.RequestParser()
        parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be blank.'
    )
        parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be blank.'
        )

        def post(self): 
            data = UserRegister.parser.parse_args()
            if User.find_by_username(data['username']):
                return{"message":"A user with that username already exists"},400                
            Connection = sqlite3.connect('data.db')
            cursor = Connection.cursor()
            query = "INSERT INTO users VALUES (NULL,?,?)"
            cursor.execute(query,(data['username'],data['password']))
            Connection.commit()
            Connection.close()  
            return{"message":"user created sucessfully."},201                  
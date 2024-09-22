# video 5:
import sqlite3
# video 5:
from flask_restful import Resource,reqparse

# video 2:
class User:

# video 2    
    def __init__(self,_id,username,password):
# video 2        
        self.id = _id
# video 2        
        self.username = username
# video 2:        
        self.password = password 


# video 5: method 1: define function name 
    # def find_by_username(self,username):
# video 5: method 2: define function name   
    @classmethod  
    def find_by_username(cls,username):
# video 5: Establish a connection to the SQLite database named 'data.db',If the database does not exist, it will be created        
        connection = sqlite3.connect("data.db")
# video 5:Create a cursor object using the connection to execute SQL commands,Call the cursor method to get the cursor object        
        cursor = connection.cursor()
# video 5:        
        query = "SELECT * FROM  users WHERE username=?"
# viddo 5:        
        result = cursor.execute(query,(username,))
# video5:        
        row = result.fetchone()
# video 5:        
        if row:
# video 5:method 1: match all user attribute(id,name,password)
            # User = User(row[0],row[1],row[2])
# video 5:method 2: match all user attribute(id,name,password)            
            # User = cls(row[0],row[1],row[2])
# video 5:method 3: match all user attribute(id,name,password)
             return cls(*row)
        else:
# video 5:            
            User = None
# video 5:Close the connection to the database       
        connection.close()
        return User  
            
# method 1: define function name 
    # def find_by_username(self,username):
# method 2: define function name    
    @classmethod    
    def find_by_id(cls,_id):
# video 5: Establish a connection to the SQLite database named 'data.db',If the database does not exist, it will be created               
        Connection = sqlite3.connect("data.db")
# video 5:Create a cursor object using the connection to execute SQL commands,Call the cursor method to get the cursor object               
        cursor = Connection.cursor()
# video 5:        
        query = "SELECT * FROM  users WHERE id=?"
# video 5:        
        result = cursor.execute(query,(_id,))
# video 5:        
        row = result.fetchone()
        if row:
# # viideo 5:method 1: match all user attribute(id,name,password)
            # User = User(row[0],row[1],row[2])
# video 5: video5method 2: match all user attribute(id,name,password)            
            # User = cls(row[0],row[1],row[2])
# video 5: method 3: match all user attribute(id,name,password)
            return cls(*row)
        else:
            User = None
# video 5:Close the connection to the database            
        Connection.close()
#  video 5:        
        return User            

# video 6: create a class user register.    
class UserRegister(Resource):
# video 6:
        parser =reqparse.RequestParser()
        parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be blank.'
    )
# video 6:        
        parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be blank.'
        )
# create a method name post.
        def post(self):
# video 6:            
            data = UserRegister.parser.parse_args()
# video 7:
            if User.find_by_username(data['username']):
# video 7:                
                return{"message":"A user with that username already exists"},400                
# video 6:            
            Connection = sqlite3.connect('data.db')
# video 6:            
            cursor = Connection.cursor()
# video 6:
            query = "INSERT INTO users VALUES (NULL,?,?)"
# video 6":            
            cursor.execute(query,(data['username'],data['password']))
# video 6:            
            Connection.commit()
# video 6:            
            Connection.close()  
# video 6:
            return{"message":"user created sucessfully."},201                  
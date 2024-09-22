# video 5:
import sqlite3
# video 5:
from flask_restful import Resource,reqparse
# video 5:
from models.user import UserModel


# video 5: create a class user register.    
class UserRegister(Resource):
# video 5:
        parser =reqparse.RequestParser()
        parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be blank.'
    )
# video 5:        
        parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be blank.'
        )
# create a method name post.
        def post(self):
# video 5:            
            data = UserRegister.parser.parse_args()
# video 5:
            if UserModel.find_by_username(data['username']):
# video 5:                
                return{"message":"A user with that username already exists"},400  
# video 10: method 1:
        #     user = UserModel(data['username'],data['password'])
# video 10: method 2:        
            user = UserModel(**data)
            user.save_to_db()                             
# video 5:            
        #     Connection = sqlite3.connect('data.db')
# video 5:            
        #     cursor = Connection.cursor()
# video 5:
        #     query = "INSERT INTO users VALUES (NULL,?,?)"
# video 5":            
        #     cursor.execute(query,(data['username'],data['password']))
# video 5:            
        #     Connection.commit()
# video 5:            
        #     Connection.close()  
# video 5:
        #     return{"message":"user created sucessfully."},201                  
        

# module:
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
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
            if UserModel.find_by_username(data['username']):
                return{"message":"A user with that username already exists"},400  
        #   user = UserModel(data['username'],data['password']) # method 1
            user = UserModel(**data) # method 2
            user.save_to_db()                             
        #     Connection = sqlite3.connect('data.db')
        #     cursor = Connection.cursor()
        #     query = "INSERT INTO users VALUES (NULL,?,?)"
        #     cursor.execute(query,(data['username'],data['password']))
        #     Connection.commit()
        #     Connection.close()  
        #     return{"message":"user created sucessfully."},201                  
        
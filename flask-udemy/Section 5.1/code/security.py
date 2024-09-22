# module:
from werkzeug.security import safe_str_cmp
from user import User

# users = [ 
#     User("123","bob","qwerty")
# ]
# username_mapping = {u.username:u for u in users}
# user_id_mapping = {u.id: u for u in users}

def authenticate(username,password):
    # user = username_mapping.get(username,None) # method 1 # in memory databse
    user = User.find_by_username(username) # method 2 # with sqlite database
    # if user and user.password==password:
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):

    user_id = payload["identity"]
    # return user_id_mapping.get(user_id,None) # method 1 # in memeory database
    return User.find_by_id(user_id) # method 2 # sqlite databse

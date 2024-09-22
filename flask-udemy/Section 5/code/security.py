# video 2:
from werkzeug.security import safe_str_cmp
# video 2:
from user import User



# video 2: method 1: store data in dictionary 
# users = [
#     {
#         "id":1,
#         "username": "bob",
#         "password":"password"
#     }
# ]

# video 2: method 2: storing data as object in list 

# users = [
#     User("123","bob","qwerty")
# ]

# video 2: method 1:
# username_mapping = { "bob":{
#     "id":1,
#     "usrname":"bob",
#     "password": "password"

# }}

# video 2: method 2: this is more concise method 
# username_mapping = {u.username:u for u in users}

# video 2:method 1:
# user_id_mapping = {1:{
#     "id":1,
#     "username":"bob",
#     "password": "password"

# }}

# video 2: method 2
# user_id_mapping = {u.id: u for u in users}

# video 2:
def authenticate(username,password):

# video 2:
    # user = username_mapping.get(username,None)
    # video 6:
    user = User.find_by_username(username)
# video 2: method 1:   
    # if user and user.password==password:
# video 2: method 2:    
    if user and safe_str_cmp(user.password,password):
# video 2:
        return user

    # # concise,safest method to comparee strings ---->>
    # if user and hmac.compare_digest(user.password,password):
    #     pass

# video 2:
def identity(payload):

# video 2:
    user_id = payload["identity"]

# video 2:method 1:
    # return user_id_mapping.get(user_id,None)
# video 5:methodb 2:
    return User.find_by_id(user_id)

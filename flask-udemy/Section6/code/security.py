# video 5:
from werkzeug.security import safe_str_cmp
# video 5:
from models.user import UserModel

# video 5:
def authenticate(username,password):

# video 5:
    # user = username_mapping.get(username,None)
    # video 5:
    user = UserModel.find_by_username(username)
# video 5: method 1:   
    # if user and user.password==password:
# video 5: method 2:   compare user and  password 
    if user and safe_str_cmp(user.password,password):
# video 5:
        return user

    # # concise,safest method to comparee strings ---->>
    # if user and hmac.compare_digest(user.password,password):
    #     pass

# video 5:
def identity(payload):

# video 5:
    user_id = payload["identity"]

# video 5:method 1:
    # return user_id_mapping.get(user_id,None)
# video 5:methodb 2:
    return UserModel.find_by_id(user_id)

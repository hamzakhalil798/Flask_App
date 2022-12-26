# from werkzeug.security import safe_str_cmp
from resources.user import UserModel

from resources.user import UserRegister
def authenticate(username, password):
  user = UserModel.find_by_username(username) 
  # use safe_str_comparison(safe_str_cmp) instead of == as == can change between python versions 
  if user.password==password:
    return user

def identity(payload):
  user_id = payload['identity']
  return UserModel.find_by_id(user_id)
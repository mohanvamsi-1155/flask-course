from models.user import UserModel

def authenticate (username,password):
    print(username)
    user = UserModel.find_by_username(username)
    print(user)
    if user and user.password == password:
        return user

def identity(payload):
    print(payload)
    user_id = payload['identity']
    print(user_id)
    return UserModel.find_by_id(user_id)

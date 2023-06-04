import json

class User:

    def __init__(self, age, name): #屬性建構式
        self.name = name
        self.age = age

def encode_user(x): #轉換型態
    if isinstance(x, User):
        return {"age":x.age, "name":x.name, x.__class__.__name__: True}
    else:
        raise TypeError("type error")

#from json import JSONEncoder

#class UserEncoder(JSONEncoder):

    def default(self, x):
        if isinstance(x, User):
            return {"age":x.age, "name":x.name, x.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, x)
        

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user = User(23, "Lux")
userJSON = json.dumps(user, default=encode_user) #cls=UserEncoder

user_info = json.loads(userJSON, object_hook=decode_user)
print(user_info.name)
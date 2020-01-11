from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import json
import uuid

PROFILE_FILE = 'app/static/UserData/Users/User.json'


class User(UserMixin):
    def __init__(self,username):
        self.username = username
        self.id = self.get_id()

    # @property
    # def password(self):
    #     # raise AttributeError('password is not a readable attribute')
    #

    # @password.setter
    def password(self, password):
        """保存用户，密码hash，id到json文件"""
        self.password_hash = generate_password_hash(password)
        with open(PROFILE_FILE,'w+') as f:
            try:
                profiles = json.load(f)
            except ValueError:
                profiles = {}
            profiles[self.username] = [self.password_hash, self.id]
            f.write(json.dumps(profiles))

    def verify_password(self, password):
        password_hash = self.get_password_hash()
        if password_hash is None:
            return False
        return check_password_hash(password_hash, password)

    def get_password_hash(self):
        try:
            with open(PROFILE_FILE) as f:
                user_profiles = json.load(f)
                user_info = user_profiles.get(self.username, None)
                if user_info is not None:
                    return user_info[0]
        except IOError:
            return None
        except ValueError:
            return None
        return None

    def get_id(self):
        """每个用户都有一个独有的id，如果没有这个用户，就产生一个单独的id
        从文件内获取 用户id ，如果不存在 返回一个派生的uuid"""
        if self.username is not None:
            try:
                with open(PROFILE_FILE) as f:
                    user_profiles = json.load(f)
                    if self.username in user_profiles:
                        return user_profiles[self.username][1]
            except IOError:
                pass
            except ValueError:
                pass
        return str(uuid.uuid4())

    @staticmethod
    def get(user_id):
        """根据 user_id 返回 User 类变量"""
        if not user_id:
            return None
        with open(PROFILE_FILE) as f:
            user_profiles = json.load(f)
            for each in user_profiles:
                if user_profiles[each][1] == user_id:
                    return User(each)
        return None

def readUser():
    result = []
    with open('app/static/UserData/Users/User','r',encoding='UTF-8') as f:
        for each in f.readlines():
            user = each.strip('\n').strip(' ').split(' ')
            if len(user) == 2:
                result.append(user)
    return result

def writeUser(addUser):
    exist = readUser()
    print(exist)
    flag = False
    strn = ''
    for No in range(len(exist)):
        if addUser[0] == exist[No][0]:
            exist[No][1] = addUser[1]
            flag = True
        strn += (str(exist[No][0])+' '+str(exist[No][1])+'\n')
    if flag is False:
        strn += (str(addUser[0])+' '+str(addUser[1])+'\n')
    with open('app/static/UserData/Users/User','w') as f:
        f.write(strn)

def checkUserAndPassword(username, password):
    exist = readUser()
    if [username,password] in exist:
        return True
    return False

# if __name__ == "__main__":
#     user = User("bianxiaogang")
#     if user.verify_password("asdfasdf"):
#         print("yes")
#     else:
#         print("no")
#     user.password("123456")
#     if user.verify_password("123456"):
#         print("yes")
#     else:
#         print("no")




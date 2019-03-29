###########################################################
# BlogMethods 用于处理保存博客，显示博客，保存记录，删除记录等问题
###########################################################
import json
import uuid
import linecache
import time

#test
# SOURCE_FILE = "../Data/blog.json"
# LOG_FILE = '../Data/blog.log'
# web
SOURCE_FILE = 'app/Data/index.json'
LOG_FILE = 'app/Data/blog.log'

# json 格式
# [
#   title: 标题
#   permission: 权限 False为不公开 True为公开
#   time: 时间
#   introduce: 简介
#   content：博文
# ]

class Blog:
    def __init__(self, uuid=None,type="id"):
        """
        :param uuid:记录为博客的唯一标识符
        :type type:type有两种类型 id 输入 id的hash值，num 为序列数
        """
        if uuid is None:
            self.id = self.get_id()
            self.title = ""
            self.time = None
            self.introduce = ""
            self.content = ""
            self.permission = True
        else:
            if type == "id" and uuid is not None:
                self.id = uuid
            elif type == "num" and uuid is not None:
                self.id = linecache.getline(LOG_FILE, uuid).strip()
            data = self.get()
            self.title = data[0]
            self.permission = data[1]
            self.time = data[2]
            self.introduce = data[3]
            self.content = data[4]

    def delete(self,id=None):
        if id is None:
            delete_id = self.id
        else:
            delete_id = id
        try:
            with open(SOURCE_FILE, "w+") as f:
                try:
                    profiles = json.load(f)
                    if delete_id in profiles:
                        profiles.pop(delete_id)
                    else:
                        print("No Found in the Source profile")
                        return False
                    f.write(json.dumps(profiles))
                    return True
                except ValueError:
                    return False
        except:
            print("open Source file failed")
            return False

    def get_id(self):
        """
        :param title: 为文章的标题，类型为str类型
        :param time: 为时间，类型为str，格式为"m-dd hh:mm",中间用空格隔开
        :return: 返回值为id，如果存在则返回，不存在就创建一个
        """
        while True:
            id = str(uuid.uuid4())
            with open(SOURCE_FILE) as f:
                try:
                    user_profiles = json.load(f)
                except:
                    return id
                if id not in user_profiles:
                    f.close()
                    return id

    def get(self):
        try:
            with open(SOURCE_FILE) as f:
                user_profiles = json.load(f)
                if self.id in user_profiles:
                    return user_profiles[self.id]
        except IOError:
            pass
        except ValueError:
            pass
        return False

    def modify(self,type,value):
        if type == "title":
            self.title = value
        elif type == "introduce":
            self.introduce = value
        elif type == "photo":
            self.photo = value
        elif type == "content":
            self.content = value
        elif type == "time":
            self.time = value
        elif type == "data":
            self.title = value[0]
            self.permission = value[1]
            self.time = value[2]
            self.introduce = value[3]
            self.content = value[4]
        else:
            return False
        return True

    def add_title(self,title):
        self.title = title

    def add_introduce(self, introduce):
        self.introduce = introduce

    def add_content(self,content):
        self.content = content

    def add_time(self,ntime=None):
        if ntime is None:
            ntime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(ntime)
            self.time = ntime
        else:
            self.time = ntime

    def save(self):
        if self.time is None:
            self.add_time()
        profiles={}
        with open(SOURCE_FILE,'r',encoding="UTF-8") as f:
            lines = f.readlines()
            for each in lines:
                print(each)
                data = json.loads(str(each))
                print(data)
                profiles.update(data)
            profiles[self.id] = [self.title,
                                 self.permission,
                                 self.time,
                                 self.introduce,
                                 self.content]
        with open(SOURCE_FILE, 'w', encoding="UTF-8") as t:
            json.dump(profiles,t)
        with open(LOG_FILE,'r+') as f:
            log = f.read()
            print(log)
            if self.id+"\n" not in log:
                f.seek(0, 0)
                f.writelines(self.id+"\n"+str(log))

    def set_permission(self, flag=True):
        self.permission = flag

    def isPrivate(self):
        return self.permission

# if __name__ == "__main__":
#     blog = Blog()
#     blog.modify(type="title",value="asdfasdfeee")
#     blog.modify(type="introduce",value="hhhhhhh,adf我从未见过如此厚颜无耻之人")
#     blog.save()






###########################################################
# BlogMethods 用于处理保存博客，显示博客，保存记录，删除记录等问题
###########################################################
import json
import uuid
import linecache
import time
import os
import shutil

CURRENT_PATH = os.getcwd()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG', 'bmp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 博客保存方式
# 博客通过类别进行分类，没有指定类别的将分配到default类中去
# 通过 index.json 按博客类别 划分
# index 格式
# {
#   time:{ uuid:[类别,time] }, time 的格式 YYMMDDHHMM 十位数
#   assort [
#               assort_name: [uuid] # 按时间排序
#           ]
# }

# web 页面文件位置
SOURCE_FILE = 'app/static/source/blog/'
INDEX_FILE = 'app/static/source/blog/index.json'
# 测试时文件位置
# SOURCE_FILE = '../static/source/blog/'
# INDEX_FILE = '../static/source/blog/index.json'

# -------------- json 格式 ----------------
# {
#     id 标识符
#     head:
#         {
#             title 题目
#             last_fetch_time 最后上传时间 YYMMDDHHMM 十位数
#             assort 分类
#             permission 0 外部可见 1 不对外可见
#         }
#     content：
#         {
#             introduce
#             image 封面图片,图片只能是引用在 video 中的图片，删除 博客 不会删除博客
#             article 文章 article 字符串
#             message 留言
#         }
# }
HEAD = ['title', 'last_fetch_time', 'assort', 'permission']
CONTENT = ['introduce', 'image', 'article', 'message']


class Blog:
    def __init__(self, uuid=None, type="uuid"):
        """
        初始化博客类
        如果没有参数，表示为新的博客，创建通用唯一识别码
        uuid:记录为博客的唯一标识符
        type: type有两种，一种为id，表示输入的uuid为通用唯一识别码
                        另一种为num，表示输入的uuid为在博客序列号
        :type type:type有两种类型 id 输入 id的hash值，num 为序列数
        """
        if uuid is None:
            # 如果没有通用唯一识别码，表示要新生成一个博客
            self.blog = {'head': {'assort': 'default', 'permission': 0}, 'content': {}, 'id': Blog.create_uuid()}
        elif type == "uuid" and uuid is not None:
            # 表示输入的uuid为通用唯一识别码"""
            self.blog = self.get_blog_by_uuid(uuid)
        elif type == "num" and uuid is not None:
            # 表示输入的uuid为博客序列号"""
            self.blog = self.get_blog_by_num(uuid)

    def delete_blog(self):
        delete_id = self.blog['id']
        try:
            # 先读取 index_file, 获取 blog 的 路径
            with open(INDEX_FILE,'r+') as index:
                index_profile = json.load(index)
                assort_name = index_profile['time'][delete_id][0]
            source_file_path = SOURCE_FILE+assort_name+"/blog.json"
            index_profile['time'].pop(delete_id)
            index_profile["assort"][assort_name].remove(delete_id)
            with open(INDEX_FILE,'w+') as index:
                json.dump(index_profile,index)
        except:
            print("delete operation in index file failed")
            return False
        try:
            # 读取 source_profiles, 删除 相应的 博客
            with open(source_file_path,'r+') as blog_profiles:
                blogs = json.load(blog_profiles)
                blogs.pop(delete_id)
            with open(source_file_path,'w+') as blog_profiles:
                json.dump(blogs,blog_profiles)
        except:
            print("delete operation in source file failed")
            return False
        return True

    @staticmethod
    def create_uuid():
        """
        生成一个博客日志中没有使用过的通用唯一识别码 uuid
        返回值：返回值为uuid，如果存在则返回，不存在就创建一个
        """
        try:
            with open(INDEX_FILE) as f:
                index_profiles = json.load(f)
                id_set = index_profiles['time']
        except:
            id_set = {}
        while True:
            # 如果生成的uuid存在就重新生成，直到不相同为止
            id = str(uuid.uuid4())
            if id not in id_set:
                return id

    # 获取所有类别，用于 select > option
    @staticmethod
    def get_all_assort() -> list:
        with open(INDEX_FILE) as f:
            blog_profiles = json.load(f)
        ans = []
        for each in blog_profiles['assort']:
            ans.append(each)
        return ans

    # 获取 某个 类别 下 的所有 uuid 列表
    @staticmethod
    def get_blogs_by_assort(assort_name):
        with open(INDEX_FILE) as f:
            blog_profiles = json.load(f)
        if assort_name in blog_profiles['assort']:
            return blog_profiles['assort'][assort_name]
        return False

    @staticmethod
    def get_blog_by_num(num):
        try:
            with open(INDEX_FILE,'r') as f:
                index_profiles = json.load(f)
                blogs = index_profiles['time']
            # 依照时间进行排序 items -》 （id,[assort,time]）
            blogs = sorted(blogs.items(), key=lambda item:item[1][1],reverse=True)
            blog = blogs[num]
            source_file_path = SOURCE_FILE+blog[1][0]+"/blog.json"
            with open(source_file_path,'r') as f:
                blog_profiles = json.load(f)
                return blog_profiles[blog[0]]
        except BaseException as Err:
            print("get blog by num Err:" + str(Err)+", num is " + str(num))
            return False

    @staticmethod
    def get_blog_by_uuid(uuid):
        try:
            with open(INDEX_FILE,'r') as index:
                index_profiles = json.load(index)
                assort_name = index_profiles['time'][uuid][0]
            source_file_path = SOURCE_FILE+assort_name+"/blog.json"
            with open(source_file_path,'r') as blogs:
                blog_profiles = json.load(blogs)
                return blog_profiles[uuid]
        except BaseException as Err:
            print("get blog by uuid Err:" + str(Err)+", uuid is " + str(uuid))
            return False

    def write_item(self, mtype, value):
        mtype = mtype.lower()
        print("current blog is" + str(self.blog))
        print("mtype is " + mtype + ", value is " + str(value))
        if mtype in HEAD:
            self.blog['head'][mtype] = value
            return True
        elif mtype in CONTENT:
            self.blog['content'][mtype] = value
            return True
        elif mtype == "all":
            self.blog = value
            return True
        return False

    def get_item(self, mtype = "all") -> dict or bool:
        mtype = mtype.lower()
        try:
            if mtype == "id":
                return self.blog['id']
            if mtype in HEAD:
                return self.blog['head'][mtype]
            elif mtype in CONTENT:
                return self.blog['content'][mtype]
            elif mtype == "all":
                return self.blog
        except:
            return False
        return False

    @staticmethod
    def get_blog_num():
        try:
            with open(INDEX_FILE) as f:
                blog_profiles = json.load(f)
                return len(blog_profiles['time'])
        except:
            return False

    @staticmethod
    def get_current_time():
        ct = time.localtime()
        ans = 0
        for t in [ct.tm_year%100,ct.tm_mon,ct.tm_mday,ct.tm_hour,ct.tm_min]:
            ans *= 100
            ans += t
        strn = "{}-{}-{} {}:{}".format(ct.tm_year,ct.tm_mon,ct.tm_mday,ct.tm_hour,ct.tm_min)
        return [ans, strn]

    # 保存时 已经 考虑了 如果类别变化 需要进行的操作
    def save_blog(self):
        uuid = self.blog['id']
        new_assort_name = self.blog['head']['assort']
        ctime = self.get_current_time()
        current_time = ctime[0]
        self.blog['head']['last_fetch_time'] = ctime[1]
        # 打开index.json, 先读取 json
        with open(INDEX_FILE, mode='r+') as f:
            # 尝试读取 index_file
            try:
                index_profiles = json.load(f)
            except:
                index_profiles = {'time':{},'assort':{}}

        # 如果仅仅是修改已存在的博客
        if uuid in index_profiles['time']:
            old_assort_name = index_profiles['time'][uuid][0]
            # 如果类别都发生变化了，需要将原博客删除，再重新添加博客
            if old_assort_name != new_assort_name:
                self.delete_blog()
                self.save_blog()
            else:
                # 否则仅仅更新时间就可以了
                index_profiles['time'][uuid][1] = current_time
        # 如果 是 之前不存在的 类别，将 文件写到 index_profiles
        else:
            index_profiles['time'][uuid] = [new_assort_name,current_time]
            if new_assort_name in index_profiles['assort']:
                index_profiles['assort'][new_assort_name].append(uuid)
            else:
                index_profiles['assort'][new_assort_name] = [uuid]
        # 将 index_profile 写入文件中
        with open(INDEX_FILE,mode="w+") as f:
            json.dump(index_profiles,f)

        source_path = SOURCE_FILE+ new_assort_name
        source_file_path = source_path + "/blog.json"
        if not os.path.exists(source_path):
            os.makedirs(source_path)
            with open(source_file_path,mode="w+") as f:
                blog_profiles = {uuid: self.blog}
                json.dump(blog_profiles,f)
        else:
            with open(source_file_path, mode="r+") as f:
                try:
                    blog_profiles = json.load(f)
                except:
                    blog_profiles = {}
            with open(source_file_path, mode="w+") as f:
                blog_profiles[uuid] = self.blog
                json.dump(blog_profiles,f)

                
if __name__ == "__main__":

    blog = Blog()
    blog.write_item('title','测试博客五')
    blog.write_item('introduce',"测试博客五 介绍")
    blog.write_item('article',"测试博客数据五 文章内容")
    blog.save_blog()

    blog = Blog()
    blog.write_item('title', '测试博客六')
    blog.write_item('introduce', "测试博客六 介绍")
    blog.write_item('article', "测试博客数据六 文章内容")
    blog.write_item('assort','python')
    blog.save_blog()

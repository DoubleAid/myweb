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

# web 页面文件位置
# SOURCE_FILE = 'app/static/source/blog/'
# INDEX_FILE = 'app/static/source/blog/index.json'
# 测试时文件位置
SOURCE_FILE = '../static/source/blog/'
INDEX_FILE = '../static/source/blog/index.json'

HEAD = ['title', 'last_fetch_time', 'assort', 'permission']
CONTENT = ['introduce', 'image', 'article', 'message']

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
# json 格式
# [
#   title: 标题
#   permission: 权限 False为不公开 True为公开
#   time: 时间
#   introduce: 简介
#   images: 图片名
#   content：博文
# ]

class Blog:
    def __init__(self, uuid=None,type="uuid"):
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
            self.blog = {'head': {'assort':'default'}, 'content': {}, 'id': Blog.create_uuid()}
        else:
            if type == "uuid" and uuid is not None:
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





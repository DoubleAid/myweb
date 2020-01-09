# 网站开发代码
**Warnning** 使用 pull request 何如代码，方便回退版本！！！
*****
目录  
[1. flask + nginx + uwsgi 环境搭建](#flask+nginx+uwsgi+环境搭建)  
[2. 代码结构](#代码结构)
[3. Issues 问题]()
*****

## [flask + nginx + uwsgi 环境搭建](https://github.com/DoubleAid/blog_record/blob/master/Python/002.Flask+uwsgi+nginx%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.md)

## 代码结构
```
├── webstart.py  项目启动文件，文件引入app中的create_app方法创建Flask对象
└── app
    ├── __init__.py   create_app,创建Flask对象
    ├── AssistMethod  数据类
    |   ├── BlogMethods.py  blog方法类，包括对blog的增、删、改、查、保存、读取等操作，对应的存储文件为 static/source/blog 文件夹中
    |   └── UserMethods.py  用户方法类，包括对user的增删改查，保存，读取，验证，需要保证密码的不可见性
    ├── Views  蓝图，后台响应函数：处理相应访问路由的反应，下面每一个文件都对应着一个蓝图，最后在__init__.py里整合
    |   ├── navigation  导航部分
    |   |   ├── Blog.py     以 /blog 开头的url的路由响应函数
    |   |   ├── Message.py  以 /message 开头的url的路由响应函数
    |   |   ├── Music.py    以 /music 开头的url的路由响应函数
    |   |   └── Video.py    以 /video 开头的url的路由响应函数
    |   ├── Adminstrator.py 登陆界面响应函数
    |   ├── Users.py        之前测试页面，未使用
    |   ├── main.py         homepage 页面响应 路由函数
    |   └── __init__.py     将其他蓝图集合在一起
    ├── static      静态文件部分，包括字体、存储的用户数据，js和css文件，开源函数库
    |   ├── UserData    用户数据，用来存储用户名，密码等
    |   |   └── Users   数据分为两个部分，通过 UserMethods 中的类先定位到哪个数据，然后再访问相应的用户
    |   |       ├── User.json
    |   |       └── User
    |   ├── fonts   字体文件部分
    |   |   ├── font-awesome.min.css    在静态文件中只会引用该css文件，该文件把其他字体和图标做一个整合
    |   |   └── 其他字体文件
    |   ├── js      静态函数和样式，该部分以 views文件夹 的结构作为参考
    |   |   ├── blog       blog部分，包括common(各个页面都会引用的js函数和样式)和每个网页的特殊样式和函数
    |   |   |   ├── blog_write
    |   |   |   |   ├── css
    |   |   |   |   |   ├── blog_write.css
    |   |   |   |   |   └── visibility-display.css
    |   |   |   |   └── js
    |   |   |   |       └── listener_action.js
    |   |   |   └── common
    |   |   |       └── blog_get_next.js
    |   |   ├── index
    |   |   |   └── base.css
    |   |   └── video
    |   |       └── total_video_style
    |   |           └── total_video_style_default.css
    |   ├── source      用户数据部分，包括blog，image，music，video，其他功能带实现
    |   |   ├── blog    blog存储文件，blog的存储方法和结构可以参考 BlogMethods.py 的注释
    |   |   |   ├── default
    |   |   |   ├── python
    |   |   |   └── index.json
    |   |   └── image   待实现
    |   |       ├── blog_image
    |   |       ├── error
    |   |       └── icon
    |   └── vendor      开源数据库，该部分可以google中查询相应的功能
    |       ├── bootstrap
    |       ├── ie
    |       ├── jquery
    |       └── 其他文件
    └── templates       模版，存储的是分化的 HTML 文件，包括基础文件 base.html 和 基于该文件开发的其他部分，其中有部分页面待分化   
        ├── adminstartor    名字拼错了，尴尬！！！不改了，登陆页面
        |   └── LoginIn.html
        ├── blog        blog部分
        |   ├── blog_multiply.html      多个 blog 显示界面
        |   ├── blog_single.html        单个 blog 显示界面
        |   └── blog_write.html         修改和编写 blog 显示界面
        ├── error       报错部分，其他报错功能带实现
        |   └── 404.html      404报错
        ├── homepages   欢迎界面
        |   └── homepage.html
        ├── music       音乐播放界面部分，该部分界面待构思
        |   ├── music_collection_interface.html
        |   ├── music_player_interface.html
        |   └── total_music_interface.html      音乐集 显示 界面
        ├── video
        |   └── total_video_interface.html
        └── base.html
```

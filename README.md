# myweb
the code of my website

## [flask + nginx + uwsgi 环境搭建](https://github.com/DoubleAid/blog_record/blob/master/Python/002.Flask+uwsgi+nginx%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.md)

## 代码结构
```
├── webstart.py  项目启动文件，文件引入app中的create_app方法创建Flask对象
└── app
    ├── AssistMethod
    |   ├── BlogMethods.py
    |   └── UserMethods.py
    ├── Views
    |   ├── navigation
    |   |   ├── Blog.py
    |   |   ├── Message.py
    |   |   ├── Music.py
    |   |   └── Video.py
    |   ├── Adminstrator.py
    |   ├── Users.py
    |   ├── main.py
    |   └── __init__.py
    ├── static
    |   ├── UserData
    |   |   └── Users
    |   |       ├── User.json
    |   |       └── User
    |   ├── fonts
    |   |   ├── font-awesome.min.css
    |   |   └── 其他字体文件
    |   ├── js
    |   |   ├── blog
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
    |   ├── source
    |   |   ├── blog
    |   |   |   ├── default
    |   |   |   ├── python
    |   |   |   └── index.json
    |   |   └── image
    |   |       ├── blog_image
    |   |       ├── error
    |   |       └── icon
    |   └── vendor
    |       ├── bootstrap
    |       ├── ie
    |       ├── jquery
    |       └── 其他文件
    └── templates
        ├── adminstartor
        |   └── LoginIn.html
        ├── blog
        |   ├── blog_multiply.html
        |   ├── blog_single.html
        |   └── blog_write.html
        ├── error
        |   └── 404.html
        ├── homepages
        |   └── homepage.html
        ├── music
        |   ├── music_collection_interface.html
        |   ├── music_player_interface.html
        |   └── total_music_interface.html
        ├── video
        |   └── total_video_interface.html
        └── base.html
```

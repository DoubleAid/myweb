# ---------- 导入蓝图 ----------
# 从 各个 分界面导入 蓝图
# blog 为 博客 蓝图
# music 为 音乐 蓝图
from .main import main
from .Adminstrator import adminstartor
from app.Views.navigation.Blog import blog
from app.Views.navigation.Music import music
from app.Views.navigation.Video import video
from app.Views.navigation.Message import message
from app.Views.Users import profile

# 注册蓝图
DEFAULT_BLUEPRINT = (
    (main, ''),
    (adminstartor, '/Login'),
    (blog, '/blog'),
    (music, '/music'),
    (video, '/video'),
    (message, '/message')
)


def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)

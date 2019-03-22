from .main import main
from .Adminstrator import adminstartor
from .Blog import blog
#需要注册的 蓝图列表
#gesh
DEFAULT_BLUEPRINT = (
    (main, ''),
    (adminstartor, '/Login'),
    (blog, '/blog')
)


def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)

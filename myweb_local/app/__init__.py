from flask import Flask,render_template
from app.Views import config_blueprint
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import login_user
from flask_wtf import CsrfProtect
from flask_session import Session
from app.AssistMethod.UserMethods import User
import os


# 登录
def config_login(app):
    app.secret_key = os.urandom(24)
    login_manager = LoginManager()
    login_manager.session_protection = "strong"
    login_manager.login_view = 'LoginIn'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)


# 错误代码 处理方式
def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html',e=e)


def create_app():
    app = Flask(__name__)
    config_blueprint(app)
    config_errorhandler(app)
    config_login(app)
    return app

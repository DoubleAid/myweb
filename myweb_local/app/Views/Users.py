from flask import Blueprint, render_template
from flask_login import current_user

profile = Blueprint('profile', __name__)

# declaration
DEBUG = False


@profile.route('/')
def index():
    return "hello"


@profile.route('/<user_url_slug>')
def timeline(user_url_slug):
    # 做些处理
    # return render_template('profile/timeline.html')
    return "timeline"


@profile.route('/<user_url_slug>/photos')
def photos(user_url_slug):
    # 做些处理
    # return render_template('profile/photos.html')
    return "photos"


@profile.route('/<user_url_slug>/about')
def about(user_url_slug):
    # 做些处理
    # return render_template('profile/about.html')
    return "about"


def get_current_user():
    if DEBUG:
        return "testUser"
    # noinspection PyBroadException
    try:
        name = current_user.username
    except BaseException:
        name = None
    return name

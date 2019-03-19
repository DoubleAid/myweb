from flask import Blueprint, render_template

profile = Blueprint('profile', __name__)

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
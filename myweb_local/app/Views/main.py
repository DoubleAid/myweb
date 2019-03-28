from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user, logout_user
main = Blueprint('main', __name__)


@main.route('/', methods=['GET','POST'])
def homepage():
    try:
        name = current_user.username
    except:
        name = None
    if name is not None:
        return render_template('homepages/homepage.html', user=name)
    else:
        return render_template('homepages/homepage.html')


@main.route('/Logout')
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))


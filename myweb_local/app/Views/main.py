from flask import Blueprint, render_template, url_for, redirect,request, jsonify
from flask_login import current_user, logout_user
from app.AssistMethod.BlogMethods import Blog
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

@main.route('/getnext')
def get_next_date():
    id = request.args.get('page', 0, type=int)
    blog = Blog(uuid=id, type="num")
    if blog.get_blog_num() < id:
        return jsonify(result={'page':id, 'html':None})
    else:
        data = blog.get_data()
        page = id+1
        return jsonify(result={'page':page, 'html':data})

@main.route('/Logout')
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))


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
    print(id)
    if Blog.get_blog_num() < id:
        return jsonify(result={'page': id, 'html': None})
    else:
        blog = Blog(uuid=id, type="num")
        data = blog.get_data()
        return jsonify(result={'page': id+1, 'html': data})

##########
# get_brief 函数用来获取最近发出的博客信息
@main.route('/getbrief')
def get_brief():
    print("get_brief 获取博客分类和最近编写")
    # for i in range(5):
    #     if i > Blog.get
    return jsonify(result="asdsa")
    
@main.route('/Logout')
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))


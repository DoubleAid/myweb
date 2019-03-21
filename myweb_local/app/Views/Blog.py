from flask import Blueprint,render_template,url_for

blog = Blueprint('blog',__name__)

@blog.route('/',methods = ['GET','POST'])
def multiple_blogs():
    return render_template('homepages/homepage.html')

@blog.route('/<num>')
def bloginfoshow(num=None):
    print(num)
    return 'hello'+str(num)

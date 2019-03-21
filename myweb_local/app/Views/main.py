from flask import Blueprint,render_template,url_for

main = Blueprint('main',__name__)

@main.route('/',methods = ['GET','POST'])
def homepage():
    return render_template('homepages/homepage.html')

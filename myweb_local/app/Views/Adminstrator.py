from flask import Blueprint,render_template,url_for,request,redirect
from app.AssistMethod.UserMethods import checkUserAndPassword
from .main import homepage
adminstartor = Blueprint('admin',__name__)

@adminstartor.route('/',methods = ['GET','POST'])
def homepage():
    if request.method == 'POST':
        usrname = request.form['username']
        password = request.form['password']
        result = checkUserAndPassword(usrname,password)
        if result is True:
            # return render_template('homepages/homepage.html')
            return redirect(url_for('main.homepage'))
        else:
            return render_template('adminstartor/LoginIn.html',warn = '用户名或密码错误')
    return render_template('adminstartor/LoginIn.html')


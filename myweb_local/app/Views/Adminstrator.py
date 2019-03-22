from flask import Blueprint,render_template,url_for,request,redirect
from app.AssistMethod.UserMethods import User
from flask_login import login_user,current_user

adminstartor = Blueprint('admin',__name__)

@adminstartor.route('/',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        usrname = request.form['username']
        password = request.form['password']
        user = User(usrname)
        if user.verify_password(password):
            login_user(user,remember=False)
            return redirect(url_for('main.homepage'))
        else:
            return render_template('adminstartor/LoginIn.html', warn='用户名或密码错误')
    return render_template('adminstartor/LoginIn.html')

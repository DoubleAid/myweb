from flask import Blueprint,render_template,url_for,request,redirect
from flask_login import current_user
from app.AssistMethod.BlogMethods import Blog

blog = Blueprint('blog',__name__)


@blog.route('/')
def multiple_blogs():
    try:
        name = current_user.username
    except:
        name = None
    if name is not None:
        return render_template('blog/blog_multiply.html', user=name)
    return render_template('blog/blog_multiply.html')


@blog.route('/<num>')
def bloginfoshow(num=None):
    print(num)
    return 'hello'+str(num)


@blog.route('/write',methods = ['GET','POST'])
def write_blog():
    if request.method == "POST":
        blog = Blog()
        title = request.form['title']
        introduce = request.form['introduce']
        content = request.form['content']
        if "::private" in title:
            title = title.replace("::private",'')
            blog.set_permission(flag=False)
        else:
            blog.set_permission(flag=True)
        blog.add_title(title)
        blog.add_introduce(introduce)
        blog.add_content(content)
        blog.save()
        return redirect(url_for('main.homepage'))
        # img.save("app/static/images/text.png")
        # img.save(url_for("static",filename="images/1.png"))
    # return render_template('blog/blog_write.html',user=current_user.username)
    return render_template('blog/blog_write.html')

@blog.route('/<num>/modify')
def modify(num):
    return str(num)+"modify"

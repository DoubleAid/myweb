from flask import Blueprint,render_template,url_for,request,redirect
from flask_login import current_user
from app.AssistMethod.BlogMethods import Blog
import os
import markdown
CURRENT_PATH = os.getcwd()
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
    blog = Blog(num)
    permission = blog.get_permission()
    data = blog.get_data()
    data['content'] = markdown.markdown(data['content'], output_format='html5')
    if permission is False:
        try:
            name = current_user.username
            return render_template('blog/blog_single.html',user=name ,data=data)
        except:
            return 404
    else:
        return render_template('blog/blog_single.html', data=data)


@blog.route('/page<num>')
def blogs_show_by_page(num=None):
    if num == 1:
        return

@blog.route('/write',methods = ['GET','POST'])
def write_blog():
    if request.method == "POST":
        blog = Blog()
        title = request.form['title']
        introduce = request.form['introduce']
        file = None
        try:
            file = request.files['file']
        except:
            pass
        # file_path = CURRENT_PATH+"/app/Data/Blog/"+str(blog.id)+"/1."
        # file.save("D://a.jpg")
        content = request.form['content']
        if len(title)==0 or len(introduce)==0 or len(content)==0:
            return 404
        if "::private" in title:
            title = title.replace("::private",'')
            blog.set_permission(flag=False)
        else:
            blog.set_permission(flag=True)
        blog.add_title(title)
        blog.add_introduce(introduce)
        if file is not None:
            blog.add_image(file)
        blog.add_content(content)
        blog.save()
        return redirect(url_for('blog.bloginfoshow',num = blog.id))
        # img.save("app/static/images/text.png")
        # img.save(url_for("static",filename="images/1.png"))
    # return render_template('blog/blog_write.html',user=current_user.username)
    return render_template('blog/blog_write.html')

@blog.route('/<num>/modify')
def modify(num):
    # blog = Blog(num)
    return str(num)+"modify"

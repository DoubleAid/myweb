from flask import Blueprint,render_template,url_for,request,redirect, Response
from flask_login import current_user
from app.AssistMethod.BlogMethods import Blog
import os
import markdown
CURRENT_PATH = os.getcwd()
blog = Blueprint('blog',__name__)

@blog.route('/')
def multiple_blogs():
    blog = Blog(uuid=1,type="num")
    print(blog.get_blog_num())
    if blog.get_blog_num() < 1:
        data = None
    else:
        data = blog.get_data()
    try:
        name = current_user.username
    except:
        name = None
    if name is not None:
        return render_template('blog/blog_multiply.html', user=name, data=data)
    return render_template('blog/blog_multiply.html', data=data)

@blog.route('/<num>')
def bloginfoshow(num=None):
    blog = Blog(num)
    permission = blog.get_permission()
    data = blog.get_data()
    if len(data['title']) == 0:
        return 404
    data['content'] = markdown.markdown(data['content'], output_format='html5')
    if permission is False:
        try:
            name = current_user.username
            return render_template('blog/blog_single.html',user=name, data=data)
        except:
            return 404
    else:
        return render_template('blog/blog_single.html', data=data)


@blog.route('/write',methods = ['GET','POST'])
def write_blog():
    try:
        name = current_user.username
    except:
        return redirect(url_for('admin.login'))
    print("test1")
    if request.method == "POST":
        blog = Blog()
        title = request.form['title']
        introduce = request.form['introduce']
        try:
            files = request.files.getlist('file')
            for file in files:
                blog.add_image(file)
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
        blog.add_content(content)
        blog.save()
        print("test2")
        return redirect(url_for('blog.bloginfoshow',num = blog.id))
        # img.save("app/static/images/text.png")
        # img.save(url_for("static",filename="images/1.png"))
    # return render_template('blog/blog_write.html',user=current_user.username)
    return render_template('blog/blog_write.html', user=name)


@blog.route('/<num>/modify',methods=['GET', 'POST'])
def modify(num):
    blog = Blog(num)
    try:
        name = current_user.username
    except:
        return redirect(url_for('admin.login'))
    if request.method == "POST":
        title = request.form['title']
        introduce = request.form['introduce']
        try:
            files = request.files.getlist('file')
            if len(files) != 0:
                blog.delete_images()
                for file in files:
                    blog.add_image(file)
        except:
            pass
        # file_path = CURRENT_PATH+"/app/Data/Blog/"+str(blog.id)+"/1."
        # file.save("D://a.jpg")
        content = request.form['content']
        if len(title) == 0 or len(introduce) == 0 or len(content) == 0:
            return 404
        if "::private" in title:
            title = title.replace("::private", '')
            blog.set_permission(flag=False)
        else:
            blog.set_permission(flag=True)
        blog.add_title(title)
        blog.add_introduce(introduce)
        blog.add_content(content)
        blog.save()
        return redirect(url_for('blog.bloginfoshow', num=blog.id))
        # img.save("app/static/images/text
    else:
        data = blog.get_data()
        return render_template('blog/blog_write.html', user=name, data=data)

@blog.route('/<num>/delete')
def delete(num):
    try:
        name = current_user.username
    except:
        return redirect(url_for('admin.login'))
    Blog.delete_blog(num)
    return redirect(url_for('blog.multiple_blogs'))

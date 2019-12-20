from flask import Blueprint,render_template,url_for,request,redirect, Response
from app.AssistMethod.BlogMethods import Blog
import app.Views.Users as User
import os
import markdown

CURRENT_PATH = os.getcwd()

# ------------- 声明 ---------------
# 默认获取地微博数量
default_show_blog_num = 4

blog = Blueprint('blog',__name__)


# ----------------- 显示微博 ---------
@blog.route('/')
def multiple_blogs():
    # blog 集
    blog_set = []
    # 比较 默认显示 的 数量
    if default_show_blog_num > Blog.get_blog_num():
        blog_num = Blog.get_blog_num()
    else:
        blog_num = default_show_blog_num
    # 将 对应的 blog 加入到 blog 集
    for i in range(blog_num):
        current_blog = Blog(uuid=i,type="num")
        blog_set.append(current_blog.get_item())
    # 检查 用户是否上线
    name = User.get_current_user()
    # 返回 渲染模板
    return render_template('blog/blog_multiply.html', user=name, blog_num=len(blog_set), blog_set=blog_set)

@blog.route('/<num>')
def show_blog_by_uuid(num):
    blog = Blog(num)
    permission = blog.get_item('permission')
    user_name = User.get_current_user()
    if user_name is None and permission == 1:
        return 404
    # 获取 blog 信息
    blog_info = blog.get_item()
    if not blog_info:
        return 404
    # 获取 blog content 格式
    blog_info['content']['article'] = markdown.markdown(blog_info['content']['article'], output_format='html5')
    return render_template('blog/blog_single.html',user=user_name, blog=blog_info)

@blog.route('/write',methods = ['GET','POST'])
def write_blog():
    user_name = User.get_current_user()
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
        # img.save("app/static/image/text.png")
        # img.save(url_for("static",filename="image/1.png"))
    # return render_template('blog/blog_write.html',user=current_user.username)
    return render_template('blog/blog_write.html', user=name)


@blog.route('/<num>/modify',methods=['GET', 'POST'])
def modify(num):
    current_blog = Blog(num)
    user_name = User.get_current_user()
    print(request.referrer)
    if user_name is None:
        return 404
    blog_info = current_blog.get_item()
    return render_template('blog/blog_write.html', user=user_name, blog=blog_info)

@blog.route('/<num>/delete')
def delete(num):
    name = User.get_current_user()
    if name is None:
        return 404
    Blog(num).delete_blog()
    return redirect(url_for('blog.multiple_blogs'))

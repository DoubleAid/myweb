from flask import Blueprint,render_template,url_for,request,redirect, Response,jsonify
from app.AssistMethod.BlogMethods import Blog
from app.Views.Users import get_current_user
import os
import markdown

CURRENT_PATH = os.getcwd()

# ------------- 声明 ---------------
# 默认获取地微博数量
DEFAULT_SHOW_BLOG_NUM = 4

blog = Blueprint('blog',__name__)


# ----------------- 显示微博 ---------
@blog.route('/')
def multiple_blogs():
    # blog 集
    blog_set = []
    # 比较 默认显示 的 数量
    if DEFAULT_SHOW_BLOG_NUM > Blog.get_blog_num():
        blog_num = Blog.get_blog_num()
    else:
        blog_num = DEFAULT_SHOW_BLOG_NUM
    # 将 对应的 blog 加入到 blog 集
    for i in range(blog_num):
        current_blog = Blog(uuid=i,type="num")
        blog_set.append(current_blog.get_item())
    # 检查 用户是否上线
    name = get_current_user()
    # 返回 渲染模板
    return render_template('blog/blog_multiply.html', user=name, blog_num=len(blog_set), blog_set=blog_set)


@blog.route('/<num>')
def show_blog_by_uuid(num):
    blog = Blog(num)
    permission = blog.get_item('permission')
    user_name = get_current_user()
    if user_name is None and permission == 1:
        return 404
    # 获取 blog 信息
    blog_info = blog.get_item()
    if not blog_info:
        return 404
    # 获取 blog content 格式
    print(blog_info['content']['article'])
    blog_info['content']['article'] = markdown.markdown(blog_info['content']['article'], output_format='html5')
    return render_template('blog/blog_single.html',user=user_name, blog=blog_info)

@blog.route('/modify/<num>', methods=['GET', 'POST'])
def modify(num):
    if request.method == "POST":
        if num == 0:
            # 新建博客
            current_blog = Blog()
        else:
            current_blog = Blog(num)
        receive_data = request.form
        # 如果获取 blog 失败，返回错误信息
        if not current_blog:
            return 404
        Flag = current_blog.write_item(mtype="title",value=receive_data['title']) & True
        Flag &= current_blog.write_item(mtype="permission", value=receive_data['permission'])
        Flag &= current_blog.write_item(mtype="assort", value=receive_data['assort'])
        Flag &= current_blog.write_item(mtype="introduce", value=receive_data['introduce'])
        Flag &= current_blog.write_item(mtype="article", value=receive_data['article'])
        if Flag:
            current_blog.save_blog()
        return "/blog/"+str(current_blog.get_item(mtype="id"))
    else:
        if num == 0:
            # 新建博客的创建和保存应该在POST的时候进行
            blog_info = None
        else:
            # 修改博客读取 uuid 为 num 的 blog
            current_blog = Blog(num)
            blog_info = current_blog.get_item()
        user_name = get_current_user()
        if user_name is None :
            return 404
        return render_template('blog/blog_write.html', user=user_name, blog=blog_info)

@blog.route('/<num>/delete')
def delete(num):
    name = get_current_user()
    if name is None:
        return 404
    Blog(num).delete_blog()
    return redirect(url_for('blog.multiple_blogs'))


@blog.route('/get_next_blogs')
def get_next_blogs():
    start = request.args.get('start', 0, type=int)
    length = request.args.get('length', 3, type=int)

    # start+length 与 blog的数量进行比较，选出最小的
    end_num = min(Blog.get_blog_num(),start+length)

    # 返回数据
    return_data = {'length': 0, 'blogs': [], 'next_start': end_num}

    for num in range(start,end_num):
        current_blog = Blog(type="num",uuid=num)
        blog = current_blog.get_item()
        if blog is not False:
            return_data['blogs'].append(blog)
            return_data['length'] += 1
    return jsonify(result=return_data)


@blog.route('/get_all_assort')
def get_all_assort():
    uuid = request.args.get("uuid",None)
    current_blog = Blog(uuid)
    if uuid:
        current_assort = current_blog.get_item(mtype="assort")
    else:
        current_assort = None
    all_assort = current_blog.get_all_assort()
    return_data = {"current_assort":current_assort,"assorts":all_assort}
    return jsonify(return_data)

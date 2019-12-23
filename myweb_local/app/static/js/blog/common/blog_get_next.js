/*

发送请求博客内容的博客数据都通过 /blog/get_next_brief 来获取

数据结构
{
    start: 起始博客
    length: 长度
    assort： 通过类获取， 如果assort为空， 通过 index 中的 time 获取
                        如果assort不为空， 通过 index 中的 assort 获取
    type： brief/detail detail 返回更多的数据，添加更多的判断

}
返回结构
{

}


 */


/*

sidebar 获取最近更新的博客
获取数量 3

*/

function sidebar_get_blog_brief(){

    // 发送的数据
    var send_data = {
        start:0,
        length:3
    };
    $.getJSON($SCRIPT_ROOT+"/blog/get_next_blogs",send_data,sidebar_post_blog_brief);
}

// 获取json成功后执行的函数
function sidebar_post_blog_brief(data){
    if (data.result['length'] != 0){
        var blog_brief = ''
        for(i=0;i<data.result['length'];i++){
            var blog_info = data.result['blogs'][i];
            blog_brief += ('<article class="mini-post">'+
                        '<header>'+
                            '<h3><a href="/blog/'+blog_info['id']+'">'+
                                blog_info['head']['title']+
                                '</a></h3>'+
                            '<time class="published" datetime="2019-12-12">'+
                                blog_info['head']['last_fetch_time']+
                            '</time>'+
                            '<h5>'+blog_info['content']['introduce']+'</h5>'+
                        '</header>'+
                        '<a href="/blog/'+blog_info['id']+'" class="image"><img src="../static/source/image/error/default.png" alt=""/></a>'+
                    '</article>');
        }
        document.getElementById("mini-posts").innerHTML=blog_brief;
    }
}

/*

submit 按钮 获取接下来的 4 个

*/

function button_get_next_blogs(){
    $('#submit').bind('click', button_click_action);
}

function button_click_action(){
    var send_data = {
        start: $('input[name="next_data"]').val(),
        length:3
    };
    $.getJSON($SCRIPT_ROOT+'/blog/get_next_blogs',send_data,button_post_next_blogs);
}

function button_post_next_blogs(data){
    if (data.result['length'] != 0){
        // 首先更新 下次申请的起始博客num
        $('input[name="next_data"]').val(data.result['next_start']);
        // blog_info 需要添加 一个 跳转的 定位点 <div id="jump+start_num">
        var jump_tip = '<div id="jump'+data.result['next_start']+'"></div>';
        $("div[id='article'").append(jump_tip);

        // 插入博客
        for (i=0;i<data.result['length'];i++){
            var blog_data = data.result['blogs'][i];
            var blog_info = ('<article class="post">'+
                            '<header>'+
                                '<div class="title">'+
                                    '<h2><a href="/blog/'+blog_data['id']+'">'+blog_data['head']['title']+'</a></h2>'+
                                    '<p>'+blog_data['introduce']+'</p>'+
                                '</div>'+
                                '<div class="meta">'+
                                    '<time class="published" datetime="2019-3-13">'+blog_data['head']['last_fetch_time']+'</time>'+
                                    '<a href="#" class="author">'+
                                        '<span class="name">en</span>'+
                                        '<img src="../../static/source/image/icon/twodog.jpeg" alt=""/>'+
                                    '</a>'+
                                '</div>'+
                            '</header>');
            if ('image' in blog_data['content']){
                blog_info += ('<a href="/blog/'+blog_data['id']+'" class="image featured">'+
                                    '<img src="../../../'+blog_data['content']['image']+'" alt="" />'+
                                '</a>');
            }
            else{
                blog_info += ('<a href="/blog/'+blog_data['id']+'" class="image featured">'+
                                    '<img src="../../../source/image/error/default.jpg" alt="" />'+
                                '</a>');
            }

            blog_info += ('<footer>'+
                         '<ul class="actions">'+
                            '<li>'+
                                '<a href="/blog/'+blog_data['id']+'" class="button big">继续阅读</a>'+
                            '</li>'+
                         '</ul>'+
                         '<ul class="stats">'+
                            '<li>'+
                            '<a href="#">'+blog_data['head']['assort']+'</a>'+
                            '</li>'+
                            '<li>'+
                                '<a href="#" class="icon fa-heart">0</a>'+
                            '</li>'+
                            '<li>'+
                                '<a href="#" class="icon fa-comment">0</a>'+
                            '</li>'+
                         '</ul>'+
                         '</footer>'+
                         '</article>');
            $("div[id='article'").append(blog_info);
        }
        // 跳转到标记位
        window.location.hash = "#jump"+data.result['next_start'];
    }
    else{
        document.getElementById("submit").className = "disabled button big next";
        document.getElementById("submit").innerHTML = "没有更多了";
    }
}

$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
$(function() {
    $('#submit').bind('click', function() {
        $.getJSON($SCRIPT_ROOT + '/getnext', {
            page: $('input[name="next_data"]').val()
        }, function(data) {
            $('input[name="next_data"]').val(data.result['page']);
            if (data.result['html']==null)
            {
                document.getElementById("submit").className = "disabled button big next";
                document.getElementById("submit").innerHTML = "没有更多了";
            }
            else
            {
                var html = '<article class="post">'+
                    '<header>'+
                        '<div class="title">'+
                            '<h2>'+'<a href="/blog/'+ data.result['html']['id'] +'">'+data.result['html']['title']+'</a>'+'</h2>'+
                            '<p>'+data.result['html']['introduce']+'</p>'+
                        '</div>'+
                        '<div class="meta">'+
                            '<time class="published" datetime="2019-3-13">'+data.result['html']['time']+'</time>'+
                            '<a href="#" class="author">'+
                                '<span class="name">'+'大狗'+'</span>'+
                        '</a>'+
                    '</div>'+
                '</header>'+
                '<a href="#" class="image featured">'+
                    '<img src="../static/Data/Blog/'+ data.result['html']['id']+'/'+data.result['html']['images'][0]+'" alt="" />'+
                '</a>'+
                '<footer>'+
                    '<ul class="actions">'+
                        '<li>'+
                            '<a href="/blog/'+ data.result['html']['id'] +'" class="button big">'+'继续阅读'+'</a>'+
                        '</li>'+
                    '</ul>'+
                    '<ul class="stats">'+
                        '<li>'+
                            '<a href="#" >'+'我的罗曼史'+'</a>'+
                        '</li>'+
                        '<li>'+
                            '<a href="#" class="icon fa-heart">'+'0'+'</a>'+
                        '</li>'+
                        '<li>'+
                            '<a href="#" class="icon fa-comment">'+'0'+'</a>'+
                        '</li>'+
                    '</ul>'+
                '</footer>'+
            '</article>'
        $("#article").append(html);
        }
      });
      return false;
    });
  });
  <!--function getInfo(){-->
    <!--$.getJSON($SCRIPT_ROOT + '/getbrief',function(data) {-->
        <!--&lt;!&ndash;window.alert(data.result);&ndash;&gt;-->
    <!--});-->
  }

function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function'){
        window.onload = func;
    }else{
        window.onload=function(){
            oldonload();
            func();
        }
    }
}

function t1() {
    change_button_color();
}

addLoadEvent(t1);

/* edit and preview 按钮相关监听事件 */
function change_button_color(){
    $('button[class="selected"]').css({
        "border": "2px solid red",
    });
}
//$(function(){
//    $('div[class="CodeMirror-code"]').children().on('keydown',function(event){
//        if (event.keyCode == 13) {
//            console.log(event.target);
//            $(event.target).parent().html();
//        }
//    });
//})

$('div[class="CodeMirror-code"]').keydown(enter_key_down);

function enter_key_down(event){
    if(event.keyCode ==13){
        var article_list = [];
        var selection = window.getSelection();
        if(selection.rangeCount > 0){
            console.log("有多处段落被选中，先不处理");
        }
        var range = selection.getRangeAt(0);
        if(range.collapsed){
            console.log("重合");
            console.log(range.startOffset);
        }
        content = range.startContainer;
        console.log(content.length);
        
        container = range.commonAncestorContainer;
        var pre_element = $(container).parents("pre.CodeMirror-line");
        line_num = Number(pre_element.prev().text());
        console.log(line_num);
        pres = $('div[class="CodeMirror-code"]').find("pre");
        for (i=1;i<= pres.length;i++){
            console.log($(pres[i-1]).text());
            article_list.push($(pres[i-1]).text())
        }
        $('div[class="CodeMirror-code"]').find("pre").each(function(){
            console.log($(this).text());
            article_list.push($(this).text());
        });
        console.log(article_list);
        var strn = article_list.join("\n");
        console.log('pre 获取地字符串为：'+ strn );
        console.log("当前textarea的值为");
        console.log($('textarea[name="value"]').val());
        $('textarea[name="value"]').val(strn);
        console.log("修改值之后");
        console.log($('textarea[name="value"]').val());
        $('textarea[name="value"]').val("123");
        console.log("修改值123之后");
        $('textarea[name="value"]').val();
        CodeMirror_lines = ""
        for(i=1;i<article_list.length;i++){
            CodeMirror_lines += build_CodeMirror_line(article_list[i-1],i);
        }
        $("div[class='CodeMirror-code']").html(123+CodeMirror_lines)
    }
}

function build_CodeMirror_line(word,line){
    console.log(word);
    ans = '<div style="position: relative;">'+
            '<div class="CodeMirror-gutter-wrapper" contenteditable="false" style="left: -53px;">'+
            '<div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">'+i+
            '</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-header cm-header-1">'+
            word +'</div>';
    console.log("ans为"+ans);
    return ans
}

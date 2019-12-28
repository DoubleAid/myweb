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
        // 禁止默认行为
        event.cancelBubble=true;
        event.preventDefault();
        event.stopPropagation();
        // 判断光标是不是选中了内容
        var selection = window.getSelection();
        if(selection.rangeCount > 1){
            console.log("有多处段落被选中，先不处理");
        }
        var range = selection.getRangeAt(0);
        if(range.collapsed){
            console.log("重合");
            console.log(range.startOffset);
        }
        content = range.startContainer.textContent;
        container = range.commonAncestorContainer;
        // 光标处 会将 源字符串分为两部分
        var old_line_word = content.substring(0,range.startOffset);
        var new_line_word = content.substring(range.startOffset,content.length);
        // 获取 pre 元素
        var pre_element = $(container).parents("pre.CodeMirror-line");
        // 获取 回车时 光标所在的行数
        line_num = Number(pre_element.prev().text());
        // 获取所有的行
        divs = $('div[class="CodeMirror-code"]').children();
        // 如果被修改的行数为第一行，需要特殊处理
        if(line_num == 1){
            $(divs[line_num-1]).find(".cm-header").html(old_line_word);
        }else{
            $(divs[line_num-1]).find("span").html(old_line_word);
        }
        for (i=line_num;i<divs.length;i++){
            $(divs[i]).find(".CodeMirror-linenumber").html(i+2);
        }
        $(divs[line_num-1]).after(build_CodeMirror_line(new_line_word,line_num+1));
        selection.removeAllRanges();
        var new_divs = $('div[class="CodeMirror-code"]').children();
        ele = ($(new_divs[line_num]).find("span"))[0];
        
        var range = document.createRange()
        range.setStart(($(new_divs[line_num]).find("span"))[0],0);
        range.setEnd(($(new_divs[line_num]).find("span"))[0],0);
        selection.addRange(range);
    }
}

function build_CodeMirror_line(word,line){
    console.log(word);
    ans = '<div style="position: relative;">'+
            '<div class="CodeMirror-gutter-wrapper" contenteditable="false" style="left: -53px;">'+
            '<div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">'+line+
            '</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">'+
            word +'</span></pre></div>';
    console.log("ans为"+ans);
    return ans
}

function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload !== "function"){
        window.onload = func;
    }else{
        window.onload=function(){
            oldonload();
            func();
        };
    }
}

// 文章内容按键事件响应
$('div[class="CodeMirror-code"]').keydown(enter_key_down);

function enter_key_down(event){
    // 判断光标是不是选中了内容
    var selection = window.getSelection();
    var range = selection.getRangeAt(0);
    // 光标所在的容器
    var content = range.startContainer.textContent;
    var container = range.commonAncestorContainer;
    // 光标处 会将 源字符串分为两部分
    var beforeWords = content.substring(0,range.startOffset);
    var afterWords = content.substring(range.startOffset,content.length);
    console.log("beforewords:"+beforeWords);
    console.log("afterwords:"+afterWords);
    // 行数
    var preElement = $(container).parents("pre.CodeMirror-line");
    var lineNum = Number(preElement.prev().text());
    // 点击回车键
    if(event.keyCode === 13){
        // 禁止默认行为
        event.cancelBubble=true;
        event.preventDefault();
        event.stopPropagation();
        // 如果被修改的行数为第一行，需要特殊处理
        // 获取所有的行
        let divs = $("div.CodeMirror-code").children();
        if(lineNum == 1){
            console.log("lineNum is 1");
            console.log(divs[0])
            $(divs[0]).find("span.cm-header").text(beforeWords);
        }else{
            $(divs[lineNum-1]).find("span").text(beforeWords);
        }
        newLine = create_article_line(lineNum+1,afterWords);
        for (let i=lineNum;i<divs.length;i++){
            $(divs[i]).find(".CodeMirror-linenumber").text(i+2);
        }
        $(divs[lineNum-1]).after(newLine);

        newDivs = $('div[class="CodeMirror-code"]').children();
        newRange = document.createRange();
        newRange.setStart(($(newDivs[lineNum]).find("span"))[0],0);
        newRange.setEnd(($(newDivs[lineNum]).find("span"))[0],0);
        selection.removeAllRanges();
        selection.addRange(newRange);
    }
    else if (event.keyCode === 8)
    {
        console.log("delete button down");
        console.log("beforewords:"+beforeWords);
        console.log("beforewords length:"+beforeWords.length);
        if (beforeWords.length == 0){
            event.cancelBubble=true;
            event.preventDefault();
            event.stopPropagation();
            if (lineNum > 1){

                console.log("修改删除后的行数 从第"+lineNum+"开始");
                // 将 afterwords 添加到上一行
                //// 获取前一段的内容，注意第一行特别处理
                var prevDiv = divs[lineNum-2];
                if(lineNum==2){
                    Textspan = $(prevDiv).find(".cm-header");
                }else{
                    Textspan = $(prevDiv).find("span");
                }
                startOffset = $(Textspan).text().length;
                word = $(Textspan).text() + afterWords;
                $(Textspan).text(word);
                console.log($(Textspan)[0]);
                // 确定光标位置
                var newDivs = $('div[class="CodeMirror-code"]').children();
                selection.removeAllRanges();
                var newRange = document.createRange();
                newRange.setStart(($(newDivs[lineNum-2]).find("span"))[0],0);
                newRange.setEnd(($(newDivs[lineNum-2]).find("span"))[0],0);
                selection.addRange(newRange);
                // 修改下面的行数
                for (i=lineNum;i<divs.length;i++){
                    $(divs[i]).find(".CodeMirror-linenumber").text(i);
                }
                // 删除目标行
                $(divs[lineNum-1]).remove()

            }
        }
        else if(beforeWords.length == 1){
            // 只有一个字符时, 删除会把span标签也删除掉
            event.cancelBubble=true;
            event.preventDefault();
            event.stopPropagation();
            $(range.startContainer).text(afterWords);
            console.log(afterWords);
            selection.removeAllRanges();
            var newRange = document.createRange();
            newRange.setStart(container,0);
            newRange.setEnd(container,0);
            selection.addRange(newRange);
        }
    }
}

// 内容上传
$("#submit").click(function () {
    console.log("click");
    let id = $("input#blog-id").val();
    let permission = $("input.magic-checkbox").prop("checked")?1:0;
    send_data = {
        "title":$("input.title-input").val(),
        "permission":permission,
        "introduce":$("textarea#introduce-textarea").val(),
        "article":get_article_content()
    };
    console.log(send_data)
    $.ajax({
            url:'/blog/modify/'+id,
            data:send_data,
            type:'POST',
            async:false,
            dataType:'text',
            success:function(data) {

                window.location.href=data;
            },
            error:function (XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest);
                console.log(textStatus);
                console.log(errorThrown);
            }
        });
});


function get_article_content(){
    let article_content = $("textarea.file-editor-textarea").text();
    let divs = $('div[class="CodeMirror-code"]').children();
    let line_list = [];
    for(i=0;i<divs.length;i++){
        line_list.push($(divs[i]).find("span").text().replace(/(^\s*)|(\s*$)/g, ""));
    }
    strn = line_list.join("\n");
    return strn;
}

addLoadEvent(set_article_content);
function set_article_content() {
    let article_content = $("textarea.file-editor-textarea").text();
    let line_list = article_content.split("\n");
    if(line_list.length !== 0){
        $("pre.CodeMirror-line").find("span").text(line_list[0])
    }
    if(line_list.length > 1) {
        for (let i = 2; i <= line_list.length; i++) {
            let content = line_list[i-1].replace(/(^\s*)|(\s*$)/g, "");
            $("div.CodeMirror-code").append(create_article_line(i,content))
        }
    }
}

function create_article_line(i,content){
    let ans = '<div style="position: relative;"><div class="CodeMirror-gutter-wrapper" contenteditable="false" style="left: -53px;"> ' +
        '<div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">'+i+'</div>'+
        '</div><pre class="CodeMirror-line" role="presentation"><span role="presentation" style="padding-right: 0.1px;">'+content+'</span>'+
        '</pre></div>';
    return ans;
}

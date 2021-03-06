/*
#######################################
onload 加载事件函数
#######################################
*/
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

/*
#######################################
onload 事件
#######################################
*/
// 在 CodeMirror-code 中加载文章内容
addLoadEvent(set_article_content);
// select 页面加载时获取所有类和当前类
addLoadEvent(getAllAssort);

/*
#######################################
页面加载时 在编辑框里加载文章内容
#######################################
*/
function set_article_content() {
    let article_content = $("textarea.file-editor-textarea").text();
    let line_list = article_content.split("\n");
    if(line_list.length !== 0){
        $("span.cm-header").text(line_list[0])
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

/*
#######################################
文章编辑内容按键事件响应
#######################################
*/
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
            $(divs[0]).find("span.cm-header").text(beforeWords);
        }else{
            $(divs[lineNum-1]).find("span").text(beforeWords);
        }
        newLine = create_article_line(lineNum+1,afterWords);
        for (let i=lineNum;i<divs.length;i++){
            $(divs[i]).find(".CodeMirror-linenumber").text(i+2);
        }
        $(divs[lineNum-1]).after(newLine);

        newDivs = $('div.CodeMirror-code').children();
        newRange = document.createRange();
        newRange.setStart($($(newDivs[lineNum]).find("span"))[0],0);
        newRange.setEnd($($(newDivs[lineNum]).find("span"))[0],0);
        selection.removeAllRanges();
        selection.addRange(newRange);
    }
    else if (event.keyCode === 8)
    {
        // 获取所有的行
        let divs = $("div.CodeMirror-code").children();
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
                // 确定光标位置
                var newDivs = $('div[class="CodeMirror-code"]').children();
                selection.removeAllRanges();
                var newRange = document.createRange();
                newRange.setStart(($(newDivs[lineNum-2]).find("span"))[0],1);
                newRange.setEnd(($(newDivs[lineNum-2]).find("span"))[0],1);
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
            span = $(container).parent();
            $(span).text(afterWords);
            selection.removeAllRanges();
            var newRange = document.createRange();
            newRange.setStart(span[0],0);
            newRange.setEnd(span[0],0);
            selection.addRange(newRange);
        }
    }
}

/*
#######################################
blog 内容上传
#######################################
*/
$("#submit").click(function () {
    let id = $("input#blog-id").val();
    let permission = $("input.magic-checkbox").prop("checked")?1:0;
    send_data = {
        "title":$("input.title-input").val(),
        "permission":permission,
        "assort":$("#select-option").val(),
        "introduce":$("textarea#introduce-textarea").val(),
        "article":get_article_content()
    };
    $.ajax({
            url:'/blog/modify/'+id,
            data:send_data,
            type:'POST',
            async:false,
            dataType:'text',
            success:function(data) {
                // data 为跳转页面信息
                window.location.href=data;
            },
            error:function (XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest);
                console.log(textStatus);
                console.log(errorThrown);
            }
        });
});

/* 获取文章内容 */
function get_article_content(){
    let article_content = $("textarea.file-editor-textarea").text();
    let divs = $('div[class="CodeMirror-code"]').children();
    let line_list = [$(divs[0]).find("span.cm-header").text()];
    for(i=1;i<divs.length;i++){
        line_list.push($(divs[i]).find("span").text().replace(/(^\s*)|(\s*$)/g, ""));
    }
    while(line_list[line_list.length-1] == ""){
        line_list.pop()
    }
    strn = line_list.join("  \n");
    return strn;
}

/*
#######################################
select 选取相应事件
#######################################
*/
/* select 与 input 重合，实现可编辑select */
$("#select-option").keypress(editEnableSelect);
$("#select-input").blur(editDisableSelect);
function editEnableSelect(event) {
    if ((event.keyCode || event.which || event.charCode) == 13){
        var select = $("#select-option");
        var input = select.next();
        var value = select.val();

        input.val(value);
        select.hide();
        input.show();
        input.focus()
    }
}
function editDisableSelect(event) {
    var input = $("#select-input");
    var select = input.prev();
    var value = input.val();

    var option = select.children(":first");
    option.attr("selected", true);
    option.text(value);
    option.val(value);

    select.show();
    input.hide();
}

/*
#######################################
获取 所有 assort， 并将 assort 插入到 select 中
#######################################
*/
function getAllAssort(){
    var send_data = {
        uuid:$("#blog-id").val()
    };
    console.log("get all assort");
    $.getJSON($SCRIPT_ROOT+'/blog/get_all_assort', send_data, function add_assort_option(data){
        console.log(data);
        let assortSelect = $("#select-option");
        for(let i=0;i<data['assorts'].length;i++){
            let opt = $("<option></option>");
            opt.val(data['assorts'][i]);
            opt.text(data['assorts'][i]);
            assortSelect.append(opt);
        }
        assortSelect.val(data['current_assort']);
    });
}

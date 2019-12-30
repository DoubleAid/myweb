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
    // 行数
    var preElement = $(container).parents("pre.CodeMirror-line");
    var lineNum = Number(preElement.prev().text());
    // 获取所有的行
    divs = $('div[class="CodeMirror-code"]').children();
    // 点击回车键
    if(event.keyCode === 13){
        // 禁止默认行为
        event.cancelBubble=true;
        event.preventDefault();
        event.stopPropagation();
        // 如果被修改的行数为第一行，需要特殊处理
        console.log(beforeWords);
        console.log(selection.rangeCount);
        if(lineNum === 1){
            $(divs[lineNum-1]).find(".cm-header").text(beforeWords);
        }else{
            $(divs[lineNum-1]).find("span").text(beforeWords);
        }
        newLine = $(divs[lineNum-1]).clone(true);
        newLine.find("span").text(afterWords);
        newLine.find(".CodeMirror-linenumber").text(lineNum+1);
        for (let i=lineNum;i<divs.length;i++){
            $(divs[i]).find(".CodeMirror-linenumber").text(i+2);
        }
        $(divs[lineNum-1]).after(newLine);

        selection.removeAllRanges();
        var newDivs = $('div[class="CodeMirror-code"]').children();
        var newRange = document.createRange();
        console.log(($(newDivs[lineNum]).find("span"))[0]);
        newRange.setStart(($(newDivs[lineNum]).find("span"))[0],0);
        newRange.setEnd(($(newDivs[lineNum]).find("span"))[0],0);
        selection.addRange(newRange);
    }
    else if (event.keyCode === 8)
    {
        if (beforeWords.length === 0){
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
    }
}

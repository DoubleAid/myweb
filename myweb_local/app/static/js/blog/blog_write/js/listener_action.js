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
    alert("233");
    change_button_color();
}

addLoadEvent(t1);

/* edit and preview 按钮相关监听事件 */
function change_button_color(){
    alert(234);
    $('button[class="selected"]').css({
        "border": "2px solid red",
    });
}

$('div[class="CodeMirror-scroll"]').keydown(enter_key_down);

function enter_key_down(event){
    if(event.keyCode ==13){
        var article_list = [];
        console.log(event.keyCode);
        $('div[class="CodeMirror-code"]').find("pre").each(function(){
            console.log($(this).text());
            article_list.push($(this).text());
        });
        console.log(article_list);
        var strn = article_list.join("\n")
        console.log(strn)
    }
}


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

function getCurrentMusic() {

}
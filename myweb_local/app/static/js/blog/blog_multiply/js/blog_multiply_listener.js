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
addLoadEvent(getAllAssort());
addLoadEvent(sidebar_get_blog_brief());
addLoadEvent(button_get_next_blogs());
/*
#######################################
assort select option 选项
#######################################
*/
function getAllAssort(){
    $.getJSON($SCRIPT_ROOT+'/blog/get_all_assort', function add_assort_option(data){
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
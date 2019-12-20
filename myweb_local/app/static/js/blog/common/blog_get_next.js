////$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
////function get_init_info(){
////    window.alert(10);
////    $.getJSON($SCRIPT_ROOT + '/getbrief',function(data){
////        window.alert(11);
////    });
////}
//(function (window){
//    window.onload=function(){
//        window.alert("123");
//    }
//});
function sidebar_get_blog_brif (script_root){
    $.getJSON($SCRIPT_ROOT+"/blog/")
}
$(document).ready(function(){
    $("li > a").hover(function(){
        $(this).css("color", "rgb(0,153,153)");
        }, function(){
        $(this).css("color", "rgb(255, 191, 0)");
    });
});

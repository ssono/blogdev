$(document).on('submit', '#comment_form', function(e){
  e.preventDefault();
  $.ajax({
    type:'POST',
    url:'comment/',
    cache: true,
    data:{
      text:$('#text').val(),
      csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
    },
    success:function(){
      location.reload();
    }
  });
});

$(document).ready(function(){
    $("#submit").hover(function(){
        $(this).css("color", "rgb(0,153,153)");
        }, function(){
        $(this).css("color", "rgb(255, 191, 0)");
    });
});

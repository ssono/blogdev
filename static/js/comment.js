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

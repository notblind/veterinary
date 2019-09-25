

var sections = $('section'), 
nav = $('nav'),
button = $('button');



nav.find('a').on('click', function () {
  var $el = $(this)
    , id = $el.attr('href')
    , offset = $(id).offset()
    , height_nb = $('#none-block').outerHeight();
  
  $('html, body').animate({
    scrollTop: offset.top + height_nb
  }, 1400);
  
  return false;
});

$(function(){
  $(button).bind('click', function(){
    if($(this).hasClass("buttcont")){
       $('html, body').animate({
         scrollTop: $('#5').offset().top + $('#none-block').outerHeight()
       }, 1200);
    }

    if($(this).hasClass("button-back")){
       $('html, body').animate({
         scrollTop: $('#0').offset().top 
       }, 1400);
    }
  });
});


$( document ).ready(function(){
 $( "div" ).hover(function(){ // задаем функцию при наведении курсора на элемент 
   if($(this).hasClass("doc-box")){
      $(this).find('img').css( "opacity", "0.85" );
    }
   }, function(){ // задаем функцию, которая срабатывает, когда указатель выходит из элемента  
   if($(this).hasClass("doc-box")){
      $(this).find('img').css( "opacity", "1" );
    }
  });
});


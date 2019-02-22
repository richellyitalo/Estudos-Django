const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
  $('#messages').fadeOut('fast');
}, 4000);
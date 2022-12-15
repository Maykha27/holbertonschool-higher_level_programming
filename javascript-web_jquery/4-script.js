// Write a JavaScript script that toggles the class
const $ = window.$;

$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
});

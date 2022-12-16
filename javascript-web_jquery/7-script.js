// Write a JavaScript script that fetches the character name from this URL
const $ = window.$;

const url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('div#character').text(data.name);
});

// Queries an API and fetches all movie titles and inserts them
// into the UL#list_movies tag

const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const list = data.results;
  for (let i = 0; i < list.length; i++) {
    $('UL#list_movies').append('<li>' + list[i].title + '</li>');
  }
});

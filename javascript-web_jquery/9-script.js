
// Queries an API for wind speed in SF and replaces the text of the
// div#sf_wind_speed tag with the speed
const $ = window.$;

$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (fetch) {
  $('#hello').text(fetch.hello);
});

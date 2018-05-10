// Requests name of Star Wars character URL and puts it into HTML
const url = 'https://swapi.co/api/people/5/?format=json';

$.get(url, function (data) {
  $('#character').text(data.name);
});

// Retrieves list of Star Wars movies and puts them in the list 'list_movies'
const url = 'https://swapi.co/api/films/?format=json';

$.get(url, function (data) {
  $.each(data.results, (index, movie) => {
    $('<li>' + movie.title + '</li>').appendTo('#list_movies');
  });
});

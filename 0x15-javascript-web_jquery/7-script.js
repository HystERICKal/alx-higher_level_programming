/* fetch character from url */
let the_link = 'https://swapi.co/api/people/5/?format=json';
$.get(the_link, function (data, stat) {
  $('div#character').text(data.name);
});

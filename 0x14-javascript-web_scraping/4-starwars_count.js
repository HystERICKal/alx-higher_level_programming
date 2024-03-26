#!/usr/bin/node
// number of movies printer
const request = require('request');
let countit = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const bodyStuff = JSON.parse(body);
    bodyStuff.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          countit = countit + 1;
        }
      });
    });
    console.log(countit);
  }
});

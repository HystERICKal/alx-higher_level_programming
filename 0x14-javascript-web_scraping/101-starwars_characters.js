#!/usr/bin/node
// star wars movie characters printed with this script

const request = require('request');
const theLink = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(theLink, function (err, response, body) {
  if (!err) {
    const cast = JSON.parse(body).characters;
    castDisplay(cast, 0);
  }
});

function castDisplay (cast, x) {
  request(cast[x], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (x + 1 < cast.length) {
        castDisplay(cast, x + 1);
      }
    }
  });
}

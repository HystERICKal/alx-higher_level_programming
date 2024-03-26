#!/usr/bin/node
// star wars movie characters printed with this script

const request = require('request');
const pass = process.argv[2];
const theLink = `https://swapi-api.alx-tools.com/api/films/${pass}`;

request.get(theLink, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const bodyStuff = JSON.parse(body);
    const cast = bodyStuff.characters;
    for (const i of cast) {
      request.get(i, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          const castName = JSON.parse(body);
          console.log(castName.name);
        }
      });
    }
  }
});

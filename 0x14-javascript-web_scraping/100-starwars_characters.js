#!/usr/bin/node
// movie characters of star wars movie printed

const request = require('request');

const pass = process.argv.slice(2)[0];
const theLink = `https://swapi-api.hbtn.io/api/films/${pass}`;

request(theLink, (error, res, body) => {
  if (error) console.log(error);
  const cast = JSON.parse(body).characters;
  for (const i in cast) {
    request(cast[i], (error, res, body) => {
      if (error) console.log(error);
      console.log(JSON.parse(body).name);
    });
  }
});

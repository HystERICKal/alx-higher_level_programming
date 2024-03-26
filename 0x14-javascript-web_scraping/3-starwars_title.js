#!/usr/bin/node
// Printing star wars movie title

const request = require("request");

const digi = process.argv.slice(2)[0];
const the_link = `https://swapi-api.hbtn.io/api/films/${digi}`;

request(the_link, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const output = JSON.parse(body).title;
  console.log(output);
});


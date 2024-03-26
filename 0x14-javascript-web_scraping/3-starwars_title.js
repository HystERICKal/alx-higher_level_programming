#!/usr/bin/node
// Printing star wars movie title

const request = require('request');

const digi = process.argv.slice(2)[0];
const theLink = `https://swapi-api.hbtn.io/api/films/${digi}`;

request(theLink, (err, res, body) => {
  if (err) console.log(err);
  const result = JSON.parse(body).title;
  console.log(result);
});

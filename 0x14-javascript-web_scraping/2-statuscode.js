#!/usr/bin/node
/* this script will display the status code of a GET request */

const request = require('request');

const url = process.argv.slice(2)[0];

request(url, (err, res, body) => {
  (err) ? console.log(err) : console.log(`code: ${res.statusCode}`);
});

#!/usr/bin/node
// grab webpage content

const request = require('request');
const fs = require('fs');

const temp = process.argv.slice(2);
const theLink = temp[0];
const theSource = temp[1];

request
  .get(theLink)
  .on('error', err => { console.log(err); })
  .pipe(fs.createWriteStream(theSource, 'utf-8'));

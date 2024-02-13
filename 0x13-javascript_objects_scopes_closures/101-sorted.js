#!/usr/bin/node
const dict = require('./101-data').dict;
const the_values = Object.values(dict);
const the_keys = Object.keys(dict);
const output = {};
let syncc;
let x = 0;

while (x < the_values.length) {
  output[JSON.stringify(the_values[x])] = [];
  syncc = the_keys.filter(key => dict[key] === the_values[x]);
  syncc.forEach(item => output[JSON.stringify(the_values[x])].push(item));
  x++;
}
console.log(output)

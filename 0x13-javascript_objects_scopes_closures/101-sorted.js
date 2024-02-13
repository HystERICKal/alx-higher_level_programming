#!/usr/bin/node
const the_dict = require('./101-data.js').the_dict;
const reslt = {
  1: Object.keys(the_dict).filter(key => the_dict[key] === 1),
  2: Object.keys(the_dict).filter(key => the_dict[key] === 2),
  3: Object.keys(the_dict).filter(key => the_dict[key] === 3)
};
console.log(reslt);

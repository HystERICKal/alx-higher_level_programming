#!/usr/bin/node
let holdr = 0;
exports.logMe = function (item) {
  console.log(`${holdr}: ${item}`);
  holdr++;
};

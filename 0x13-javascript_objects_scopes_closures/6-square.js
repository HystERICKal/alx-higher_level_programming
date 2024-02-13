#!/usr/bin/node
const inh_square = require('./5-square.js');

module.exports = class Square extends inh_square {
  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      let x = 0;
      while (x < this.height) {
        console.log(c.repeat(this.width));
        x++;
      }
    }
  }
};

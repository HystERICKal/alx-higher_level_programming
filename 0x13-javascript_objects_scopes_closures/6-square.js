#!/usr/bin/node
const inh_square = require('./5-square.js');

module.exports = class Square extends inh_square {
  charPrint (l) {
    if (l === undefined) { this.print(); } else {
        let x = 0;
      while (x < this.height) {
        console.log(l.repeat(this.width));
        x++;
      }
    }
  }
};

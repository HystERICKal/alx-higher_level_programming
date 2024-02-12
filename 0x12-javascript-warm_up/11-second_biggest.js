#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const the_lis = process.argv.slice(2).map(Number);
  const the_sorted = the_lis.sort(function (x, y) { 
    return y - x; 
  })[1];
  console.log(the_sorted);
}

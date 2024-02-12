#!/usr/bin/node
const digit = parseInt(process.argv[2], 10);
const resultt = 'X';
if (isNaN(digit)) {
  console.log('Missing size');
} else {
  let x = 0;
  while (x < digit) {
    console.log(resultt.repeat(digit));
    x++;
  }
}

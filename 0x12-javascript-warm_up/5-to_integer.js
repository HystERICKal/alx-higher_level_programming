#!/usr/bin/node
const digit = parseInt(process.argv[2], 10);
if (!digit) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}

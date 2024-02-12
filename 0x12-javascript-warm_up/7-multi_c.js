#!/usr/bin/node
const digit = parseInt(process.argv[2], 10);
if (isNaN(digit)) {
  console.log('Missing number of occurences');
} else {
    let x = 0;
  while (x < process.argv[2]){
     console.log('C is fun');
     x++;
  }
}

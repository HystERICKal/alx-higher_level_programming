#!/usr/bin/node
const digit = parseInt(process.argv[2]);
function factorial (dig) {
  if (isNaN(dig) || dig === 0) return (1);
  return (dig * factorial(dig - 1));
}
console.log(factorial(digit));

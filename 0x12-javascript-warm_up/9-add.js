#!/usr/bin/node
// prints the addition of 2 integers

function sum (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

sum(process.argv[2], process.argv[3]);

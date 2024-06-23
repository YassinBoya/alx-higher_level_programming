#!/usr/bin/node
// prints the first argument passed to teh command

if (process.argv[2] == null) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}

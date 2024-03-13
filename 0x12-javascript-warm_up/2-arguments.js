#!/usr/bin/node

const { argv } = require('node:process');

// The 'argv' array always contains at least two elements:
// [0] path to node, [1] path to the script file.
// Additional arguments are from index 2 onwards.

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
}
for (let i = 0; i < argv[2]; i++) {
  console.log('x'.repeat(parseInt(argv[2])));
}

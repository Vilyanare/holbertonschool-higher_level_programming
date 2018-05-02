#!/usr/bin/node
const x = parseInt(process.argv[2]);
let i = 0;
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

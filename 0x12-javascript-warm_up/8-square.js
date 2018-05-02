#!/usr/bin/node
const size = parseInt(process.argv[2]);
let msg = '';
let i = 0;
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 1) {
  for (i = 0; i < size; i++) {
    msg += 'X';
  }
  for (i = 0; i < size; i++) {
    console.log(msg);
  }
}

#!/usr/bin/node
const lenArgs = process.argv.length;
let i = 0;
let max = -Infinity;
if (lenArgs < 4) {
  console.log(0);
} else {
  for (i = 1; i < lenArgs; i++) {
    if (parseInt(process.argv[i]) > max) {
      max = parseInt(process.argv[i]);
    }
  }
  console.log(max);
}

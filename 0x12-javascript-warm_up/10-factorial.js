#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (a) {
  if (a !== 0) {
    return (a * factorial(a - 1));
  } else {
    return (1);
  }
}
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}

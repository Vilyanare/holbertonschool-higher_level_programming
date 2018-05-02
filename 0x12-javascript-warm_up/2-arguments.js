#!/usr/bin/node
const lenArgv = process.argv.length;
if (lenArgv < 3) {
  console.log('No argument');
}
if (lenArgv === 3) {
  console.log('Argument found');
}
if (lenArgv > 3) {
  console.log('Arguments found');
}

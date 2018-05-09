#!/usr/bin/node
// Opens a file and prints what's inside
const fs = require('fs');
let filePath = './' + process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});

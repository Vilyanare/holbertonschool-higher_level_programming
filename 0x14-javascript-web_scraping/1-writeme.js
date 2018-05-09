#!/usr/bin/node
// Writes provided string to provided file
const fs = require('fs');
const filePath = process.argv[2];
const txt = process.argv[3];

fs.writeFile(filePath, txt, 'utf8', (err) => {
  if (err) console.log(err);
});

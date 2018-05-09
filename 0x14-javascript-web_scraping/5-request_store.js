#!/usr/bin/node
// Saves contents of provided URL to provided file
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, resp, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});

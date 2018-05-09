#!/usr/bin/node
// Displays the status code of a get request to provided URI
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.log(err);
  else console.log(response.statusCode);
});

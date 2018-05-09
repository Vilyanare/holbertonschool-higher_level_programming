#!/usr/bin/node
// Pings Star Wars API to find a specific film based on provided ID
const request = require('request');
const filmID = process.argv[2];
const url = 'http://swapi.co/api/films/' + filmID;

request(url, (err, response, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body)['title']);
});

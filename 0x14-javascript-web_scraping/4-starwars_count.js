#!/usr/bin/node
// Pings starwars API to find out how many films "Wedge Antilles" shows up in
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) console.log(err);
  else {
    const jsonBody = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < jsonBody['results'].length; i++) {
      if (jsonBody['results'][i]['characters'].indexOf('https://swapi.co/api/people/18/') > -1) {
        count++;
      }
    }
    console.log(count);
  }
});

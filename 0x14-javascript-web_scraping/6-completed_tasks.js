#!/usr/bin/node
// Displays number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) console.log(err);
  else {
    const jsonBody = JSON.parse(body);
    let results = {};
    let userID;
    for (let i = 0; i < jsonBody.length; i++) {
      userID = jsonBody[i]['userId'];
      if (jsonBody[i]['completed'] === true) {
        if (results[userID]) {
          results[userID]++;
        } else {
          results[userID] = 1;
        }
      }
    }
    console.log(results);
  }
});

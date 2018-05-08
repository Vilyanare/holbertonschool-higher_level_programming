#!/usr/bin/node
// Prints the value of item plus number of times function has been called
// Format:
//  "<numberOfTimes>: <item>" "0: Hello"
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};

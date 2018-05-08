#!/usr/bin/node
const previoiusSquare = require('./5-square.js');

class Square extends previoiusSquare {
  // Class square describes a square that inherits from previous square
  charPrint (c = 'X') {
    // Prints a text representation of the rectangle with X unless provided with char
    let temp = '';
    for (let cw = 0; cw < this.width; cw++) {
      temp += c;
    }
    for (let ch = 0; ch < this.height; ch++) {
      console.log(temp);
    }
  }
}

module.exports = Square;

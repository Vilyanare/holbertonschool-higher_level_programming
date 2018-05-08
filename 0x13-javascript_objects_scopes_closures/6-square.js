#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  // Class square describes a square that inherits from rectangle
  constructor (size) {
    // Initializes square with width and height based on rectangles constructor
    super(size, size);
  }

  charPrint (c = 'X') {
    // Prints a text representation of the rectangle with X unless provided with char
    let cw = 0;
    let ch = 0;
    let temp = '';
    for (cw = 0; cw < this.width; cw++) {
      temp += c;
    }
    for (ch = 0; ch < this.height; ch++) {
      console.log(temp);
    }
  }
}

module.exports = Square;

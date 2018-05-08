#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  // Class square describes a square that inherits from rectangle
  constructor (size) {
    // Initializes square with width and height based on rectangles constructor
    super(size, size);
  }
}

module.exports = Square;

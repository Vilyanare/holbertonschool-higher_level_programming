#!/usr/bin/node
class Rectangle {
  // Class that describes a rectangle with width and height
  constructor (w, h) {
    // constructor that initializes width and height
    // if either are below 1 makes an empty class
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

#!/usr/bin/node
class Rectangle {
  // Class that describes a rectangle with width and height
  // Methods:
  //  print
  //  double
  //  rotate
  constructor (w, h) {
    // constructor that initializes width and height
    // if either are below 1 makes an empty class
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Prints a text representation of the rectangle with X's
    let cw = 0;
    let ch = 0;
    let temp = '';
    for (cw = 0; cw < this.width; cw++) {
      temp += 'X';
    }
    for (ch = 0; ch < this.height; ch++) {
      console.log(temp);
    }
  }

  double () {
    // Doubles the height and width of the rectangle
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    // Switches values of height and width
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}

module.exports = Rectangle;

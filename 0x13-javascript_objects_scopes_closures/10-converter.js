#!/usr/bin/node
// Converts number to given base
exports.converter = function (base) {
  function convert (value) {
    return value.toString(base);
  }
  return convert;
};

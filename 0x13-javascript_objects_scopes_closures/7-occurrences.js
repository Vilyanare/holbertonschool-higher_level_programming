#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Finds number of occurences of searchElement in list
  var count = 0;
  list.forEach(function (item) {
    if (item === searchElement) {
      count++;
    }
  });
  return (count);
};

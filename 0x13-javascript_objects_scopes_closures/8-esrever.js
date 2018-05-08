#!/usr/bin/node
exports.esrever = function (list) {
  // Returns reversed version of passed list
  let newList = [];
  const len = list.length;
  for (let i = 0; i < len; i ++) {
    newList.push(list.pop());
  }
  return (newList);
};

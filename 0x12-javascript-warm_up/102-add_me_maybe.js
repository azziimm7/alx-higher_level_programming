#!/usr/bin/node
exports.addMeMaybe = function (number, someFunction) {
  someFunction(++number);
};

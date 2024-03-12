#!/usr/bin/node
exports.callMeMoby = function (count, someFunction) {
  for (let i = 0; i < count; i++) someFunction();
};

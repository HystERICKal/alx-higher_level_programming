#!/usr/bin/node
exports.esrever = function (list) {
  const reslt = [];
  let x = list.length - 1;
  while (x >= 0) {
    reslt.push(list[x]);
    x--;
  }
  return (reslt);
};

#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let reslt = 0;
  let x = 0;
  while (x < list.length) {
    if (list[x] === searchElement) reslt++;
    x++;
  }
  return (reslt);
};

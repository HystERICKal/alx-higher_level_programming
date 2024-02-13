#!/usr/bin/node

exports.converter = function (base) {
  return function (args) {
    return args.toString(base);
  };
};

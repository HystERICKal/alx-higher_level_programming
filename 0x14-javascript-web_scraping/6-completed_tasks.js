#!/usr/bin/node
// How many tasks completed?
const request = require('request');

const theLink = process.argv[2];
const temp = {};

function count (doTask) {
  if (doTask.completed) {
    const userId = doTask.userId.toString();
    temp[userId] = temp[userId] + 1 || 1;
  }
}

request(theLink, (err, response, body) => {
  if (err) throw err;
  if (response.statusCode === 200) {
    JSON.parse(body).forEach(count);
    console.log(temp);
  }
});

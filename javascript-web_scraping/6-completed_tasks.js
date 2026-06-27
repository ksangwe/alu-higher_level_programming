#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const todos = JSON.parse(body);
  const completed = {};
  for (const todo of todos) {
    if (todo.completed) {
      if (completed[todo.userId] === undefined) {
        completed[todo.userId] = 0;
      }
      completed[todo.userId]++;
    }
  }
  console.log(completed);
});

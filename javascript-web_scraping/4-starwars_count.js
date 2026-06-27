#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    if (film.characters.includes(wedge)) {
      count++;
    }
  }
  console.log(count);
});

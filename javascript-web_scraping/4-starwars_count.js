#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('/people/18/')) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});

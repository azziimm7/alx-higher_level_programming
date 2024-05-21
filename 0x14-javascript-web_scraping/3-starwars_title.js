#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const ApiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(ApiUrl + episode, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const JsonBody = JSON.parse(body);
    console.log(JsonBody.title);
  } else {
    console.log(response.statusCode);
  }
});

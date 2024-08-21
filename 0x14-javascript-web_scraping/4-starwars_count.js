#!/usr/bin/node

const request = require('request');

const starWarsUrl = 'https://swapi-api.alx-tools.com/api/films/';

request('https://swapi-api.alx-tools.com/api/films/', function (error, response, body) {
  body =  JSON.parse(body).results;
  for(let i = 0; i <body.length; i++){
    
    for(let i = 0; i <body.length; i++){
        console.log(body[i].characters);
       
      }
  }
});

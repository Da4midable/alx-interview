#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movieData = JSON.parse(body);

  if (response.statusCode !== 200) {
    console.error('Error: Movie not found');
    return;
  }

  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      const characterData = JSON.parse(charBody);

      console.log(characterData.name);
    });
  });
});

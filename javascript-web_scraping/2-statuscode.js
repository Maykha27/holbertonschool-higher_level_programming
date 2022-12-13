#!/usr/bin/node
// Write a script that display the status code of a GET request.

const requestMod = require('request');
requestMod(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

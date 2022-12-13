#!/usr/bin/node
// Write a script that reads and prints the content of a file.

const filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

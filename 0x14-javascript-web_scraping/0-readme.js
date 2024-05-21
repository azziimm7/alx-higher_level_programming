#!/usr/bin/node

// inlude fs module
const fs = require('fs');
const filename = process.argv[2];

// use fs.readfile to read content
fs.readFile(filename, 'utf-8', function (err, data) {
  // Display file content or err
  console.log(err || data);
});

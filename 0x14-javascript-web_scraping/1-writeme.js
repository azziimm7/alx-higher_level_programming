#!/usr/bin/node

const fs = require("fs");
const file = process.argv[2]
const data = process.argv[3]

// using fs.writeFile method
fs.writeFile(file, data, 'utf-8', (err) => {
  if (err)
    console.log(err);
});

#!/usr/bin/node
const Argc = process.argv.length;
if (Argc === 2) console.log('No argument');
else if (Argc === 3) console.log('Argument found');
else console.log('Arguments found');

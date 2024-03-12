#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < num; r++) {
    let row = '';
    for (let c = 0; c < num; c++) row += 'X';
    console.log(row);
  }
}

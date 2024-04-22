#!/usr/bin/node

const data = 'C is fun';

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  if (process.argv[2] > 0) {
    for (let i = 0; i < process.argv[2]; i++) {
      console.log(data);
    }
  }
}

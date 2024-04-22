#!/usr/bin/node

function factorial (n) {
  let out = 1;
  for (let i = 1; i <= n; i++) {
    out *= i;
  }
  return (out);
}

const arg = process.argv[2];

if (isNaN(factorial(arg))) {
  console.log('1');
} else {
  console.log(factorial(arg));
}

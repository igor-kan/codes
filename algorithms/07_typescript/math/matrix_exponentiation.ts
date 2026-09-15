// Fibonacci by matrix exponentiation.
type Matrix = number[][];

function multiply(a: Matrix, b: Matrix): Matrix {
  const r: Matrix = [[0, 0], [0, 0]];
  for (let i = 0; i < 2; i += 1)
    for (let j = 0; j < 2; j += 1)
      for (let k = 0; k < 2; k += 1) r[i][j] += a[i][k] * b[k][j];
  return r;
}

function fib(n: number): number {
  let result: Matrix = [[1, 0], [0, 1]];
  let base: Matrix = [[1, 1], [1, 0]];
  while (n > 0) {
    if (n & 1) result = multiply(result, base);
    base = multiply(base, base);
    n >>= 1;
  }
  return result[0][1];
}

if (fib(10) !== 55 || fib(20) !== 6765) throw new Error("wrong Fibonacci");
console.log(`fib(20)=${fib(20)}`);

// QR algorithm for eigenvalues.
function qrDecomposition(matrix: number[][]): { q: number[][]; r: number[][] } {
  const n = matrix.length;
  const q = Array.from({ length: n }, () => new Array<number>(n).fill(0));
  const r = Array.from({ length: n }, () => new Array<number>(n).fill(0));
  for (let j = 0; j < n; j += 1) {
    let v = matrix.map((row) => row[j]);
    for (let i = 0; i < j; i += 1) {
      r[i][j] = q.reduce((acc, column, k) => acc + column[i] * v[k], 0);
      v = v.map((value, k) => value - r[i][j] * q[k][i]);
    }
    r[j][j] = Math.sqrt(v.reduce((acc, value) => acc + value * value, 0));
    for (let k = 0; k < n; k += 1) q[k][j] = v[k] / r[j][j];
  }
  return { q, r };
}

function qrAlgorithm(matrix: number[][], iterations = 1000): number[] {
  const n = matrix.length;
  let current = matrix.map((row) => [...row]);
  for (let iteration = 0; iteration < iterations; iteration += 1) {
    const { q, r } = qrDecomposition(current);
    current = Array.from({ length: n }, (_, i) =>
      Array.from({ length: n }, (_, j) => r[i].reduce((acc, value, k) => acc + value * q[k][j], 0)));
  }
  return current.map((row, i) => row[i]).sort((a, b) => a - b);
}

const eigenvalues = qrAlgorithm([[2, 1], [1, 2]]);
if (Math.abs(eigenvalues[0] - 1) > 1e-6 || Math.abs(eigenvalues[1] - 3) > 1e-6) throw new Error("qr algorithm failed");
console.log(`eigenvalues=${eigenvalues}`);

// Jacobi eigenvalue algorithm for real symmetric matrices.
function jacobiEigenvalue(matrix: number[][]): { eigenvalues: number[]; vectors: number[][] } {
  const n = matrix.length;
  const a = matrix.map((row) => [...row]);
  const vectors = a.map((_, i) => a.map((__, j) => (i === j ? 1 : 0)));
  for (let iteration = 0; iteration < 100; iteration += 1) {
    let p = 0;
    let q = 1;
    let largest = 0;
    for (let i = 0; i < n; i += 1) {
      for (let j = i + 1; j < n; j += 1) {
        if (Math.abs(a[i][j]) > largest) { largest = Math.abs(a[i][j]); p = i; q = j; }
      }
    }
    if (largest < 1e-12) break;
    const theta = 0.5 * Math.atan2(2 * a[p][q], a[q][q] - a[p][p]);
    const c = Math.cos(theta);
    const s = Math.sin(theta);
    for (let k = 0; k < n; k += 1) {
      const akp = a[k][p];
      const akq = a[k][q];
      a[k][p] = c * akp - s * akq;
      a[k][q] = s * akp + c * akq;
    }
    for (let k = 0; k < n; k += 1) {
      const apk = a[p][k];
      const aqk = a[q][k];
      a[p][k] = c * apk - s * aqk;
      a[q][k] = s * apk + c * aqk;
    }
    for (let k = 0; k < n; k += 1) {
      const vkp = vectors[k][p];
      const vkq = vectors[k][q];
      vectors[k][p] = c * vkp - s * vkq;
      vectors[k][q] = s * vkp + c * vkq;
    }
  }
  return { eigenvalues: a.map((row, i) => row[i]), vectors };
}

const { eigenvalues } = jacobiEigenvalue([[4, 1, 0], [1, 3, 1], [0, 1, 2]]);
const sum = eigenvalues.reduce((acc, v) => acc + v, 0);
const product = eigenvalues.reduce((acc, v) => acc * v, 1);
if (Math.abs(sum - 9) > 1e-9 || Math.abs(product - 18) > 1e-9) throw new Error("jacobi eigenvalues failed");
console.log(`eigenvalues=${eigenvalues}`);

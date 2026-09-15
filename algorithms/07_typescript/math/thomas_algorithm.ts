// Thomas algorithm for tridiagonal systems.
function thomasAlgorithm(lower: number[], diagonal: number[], upper: number[], rhs: number[]): number[] {
  const n = diagonal.length;
  const c = new Array<number>(n).fill(0);
  const d = new Array<number>(n).fill(0);
  c[0] = upper[0] / diagonal[0];
  d[0] = rhs[0] / diagonal[0];
  for (let i = 1; i < n; i += 1) {
    const denominator = diagonal[i] - lower[i] * c[i - 1];
    c[i] = i < n - 1 ? upper[i] / denominator : 0;
    d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator;
  }
  const x = new Array<number>(n).fill(0);
  x[n - 1] = d[n - 1];
  for (let i = n - 2; i >= 0; i -= 1) x[i] = d[i] - c[i] * x[i + 1];
  return x;
}

const x = thomasAlgorithm([0, -1, -1], [2, 2, 2], [-1, -1, 0], [1, 0, 1]);
if (x.some((value) => Math.abs(value - 1) > 1e-12)) throw new Error("thomas failed");
console.log(`x=${x}`);

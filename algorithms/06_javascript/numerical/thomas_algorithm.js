function thomasAlgorithm(lower, diagonal, upper, rhs) {
  const n = diagonal.length;
  const c = new Array(n).fill(0);
  const d = new Array(n).fill(0);
  c[0] = upper[0] / diagonal[0];
  d[0] = rhs[0] / diagonal[0];
  for (let i = 1; i < n; i += 1) {
    const denominator = diagonal[i] - lower[i] * c[i - 1];
    c[i] = i < n - 1 ? upper[i] / denominator : 0;
    d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator;
  }
  const x = new Array(n).fill(0);
  x[n - 1] = d[n - 1];
  for (let i = n - 2; i >= 0; i -= 1) x[i] = d[i] - c[i] * x[i + 1];
  return x;
}

module.exports = { thomasAlgorithm };

if (require.main === module) {
  const x = thomasAlgorithm([0, -1, -1], [2, 2, 2], [-1, -1, 0], [1, 0, 1]);
  if (x.some((value) => Math.abs(value - 1) > 1e-12)) throw new Error("thomas algorithm failed");
  console.log("[JavaScript Thomas Algorithm] tridiagonal solve verified");
}

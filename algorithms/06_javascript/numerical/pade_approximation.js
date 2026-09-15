function solve(matrix, rhs) {
  const n = rhs.length;
  const a = matrix.map((row, i) => [...row, rhs[i]]);
  for (let col = 0; col < n; col += 1) {
    let pivot = col;
    for (let r = col + 1; r < n; r += 1) if (Math.abs(a[r][col]) > Math.abs(a[pivot][col])) pivot = r;
    [a[col], a[pivot]] = [a[pivot], a[col]];
    for (let r = col + 1; r < n; r += 1) {
      const factor = a[r][col] / a[col][col];
      for (let k = col; k <= n; k += 1) a[r][k] -= factor * a[col][k];
    }
  }
  const x = new Array(n).fill(0);
  for (let r = n - 1; r >= 0; r -= 1) {
    x[r] = (a[r][n] - a[r].slice(r + 1, n).reduce((acc, value, k) => acc + value * x[r + 1 + k], 0)) / a[r][r];
  }
  return x;
}

function padeCoefficients(series, numeratorDegree, denominatorDegree) {
  const matrix = Array.from({ length: denominatorDegree }, (_, i) =>
    Array.from({ length: denominatorDegree }, (_, j) => series[numeratorDegree + (i + 1) - (j + 1)]));
  const rhs = Array.from({ length: denominatorDegree }, (_, i) => -series[numeratorDegree + i + 1]);
  const denominator = solve(matrix, rhs);
  const numerator = Array.from({ length: numeratorDegree + 1 }, (_, i) => {
    let term = series[i];
    for (let j = 1; j <= Math.min(i, denominatorDegree); j += 1) term += denominator[j - 1] * series[i - j];
    return term;
  });
  return { numerator, denominator };
}

function padeEvaluate(numerator, denominator, x) {
  const num = numerator.reduce((acc, c, i) => acc + c * x ** i, 0);
  const den = [1, ...denominator].reduce((acc, c, i) => acc + c * x ** i, 0);
  return num / den;
}

module.exports = { padeCoefficients, padeEvaluate };

if (require.main === module) {
  const series = [1, 1, 0.5, 1 / 6, 1 / 24];
  const { numerator, denominator } = padeCoefficients(series, 2, 2);
  if (Math.abs(padeEvaluate(numerator, denominator, 1) - 19 / 7) > 1e-9) throw new Error("pade failed");
  console.log("[JavaScript Pade Approximation] [2/2] of exp verified");
}

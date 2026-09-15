// Pade approximation from a Taylor series.
function solve(matrix: number[][], rhs: number[]): number[] {
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
  const x = new Array<number>(n).fill(0);
  for (let r = n - 1; r >= 0; r -= 1) {
    let sum = a[r][n];
    for (let k = r + 1; k < n; k += 1) sum -= a[r][k] * x[k];
    x[r] = sum / a[r][r];
  }
  return x;
}

function padeCoefficients(series: number[], numeratorDegree: number, denominatorDegree: number): { numerator: number[]; denominator: number[] } {
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

function padeEvaluate(numerator: number[], denominator: number[], x: number): number {
  const num = numerator.reduce((acc, c, i) => acc + c * x ** i, 0);
  const den = [1, ...denominator].reduce((acc, c, i) => acc + c * x ** i, 0);
  return num / den;
}

const series = [1, 1, 0.5, 1 / 6, 1 / 24];
const { numerator, denominator } = padeCoefficients(series, 2, 2);
if (Math.abs(padeEvaluate(numerator, denominator, 1) - 19 / 7) > 1e-9) throw new Error("pade failed");
console.log(`[2/2] Pade(1)=${padeEvaluate(numerator, denominator, 1)}`);

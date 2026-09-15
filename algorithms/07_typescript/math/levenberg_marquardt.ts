// Levenberg-Marquardt least-squares fitting.
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

function levenbergMarquardt(
  model: (x: number, p: number[]) => number,
  jacobian: (x: number, p: number[]) => number[],
  xs: number[],
  ys: number[],
  initial: number[],
  damping = 1e-3,
  maxIterations = 200,
): number[] {
  let parameters = [...initial];
  let lambda = damping;
  for (let iteration = 0; iteration < maxIterations; iteration += 1) {
    const residuals = xs.map((x, i) => ys[i] - model(x, parameters));
    const jac = xs.map((x) => jacobian(x, parameters));
    const columns = parameters.length;
    const jtj = Array.from({ length: columns }, (_, a) =>
      Array.from({ length: columns }, (_, b) => jac.reduce((acc, row) => acc + row[a] * row[b], 0)));
    const jtr = Array.from({ length: columns }, (_, a) => jac.reduce((acc, row, i) => acc + row[a] * residuals[i], 0));
    const updated = jtj.map((row, a) => row.map((value, b) => value + (a === b ? lambda : 0)));
    const delta = solve(updated, jtr);
    const candidate = parameters.map((value, i) => value + delta[i]);
    const cost = residuals.reduce((acc, r) => acc + r * r, 0);
    const candidateCost = xs.reduce((acc, x, i) => acc + (ys[i] - model(x, candidate)) ** 2, 0);
    if (candidateCost < cost) parameters = candidate; else lambda *= 10;
  }
  return parameters;
}

const xs = [0, 1, 2, 3, 4];
const ys = xs.map((x) => 1 + 2 * x + 3 * x * x);
const fitted = levenbergMarquardt((x, p) => p[0] + p[1] * x + p[2] * x * x, (x) => [1, x, x * x], xs, ys, [0, 0, 0]);
if (Math.abs(fitted[0] - 1) > 1e-6 || Math.abs(fitted[1] - 2) > 1e-6 || Math.abs(fitted[2] - 3) > 1e-6) {
  throw new Error("levenberg marquardt failed");
}
console.log(`fitted coefficients=${fitted}`);

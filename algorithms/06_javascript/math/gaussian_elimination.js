// Gaussian elimination with partial pivoting.
function solve(matrix, rhs) {
  const n = matrix.length;
  const a = matrix.map((row, i) => [...row, rhs[i]]);
  for (let c = 0; c < n; c += 1) {
    let pivot = c;
    for (let r = c + 1; r < n; r += 1) {
      if (Math.abs(a[r][c]) > Math.abs(a[pivot][c])) pivot = r;
    }
    [a[c], a[pivot]] = [a[pivot], a[c]];
    for (let r = c + 1; r < n; r += 1) {
      const factor = a[r][c] / a[c][c];
      for (let k = c; k <= n; k += 1) a[r][k] -= factor * a[c][k];
    }
  }
  const x = new Array(n).fill(0);
  for (let r = n - 1; r >= 0; r -= 1) {
    let sum = a[r][n];
    for (let k = r + 1; k < n; k += 1) sum -= a[r][k] * x[k];
    x[r] = sum / a[r][r];
  }
  return x;
}

const solution = solve([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], [8, -11, -3]);
if (Math.abs(solution[0] - 2) > 1e-9 || Math.abs(solution[1] - 3) > 1e-9 || Math.abs(solution[2] + 1) > 1e-9) {
  throw new Error("wrong solution");
}
console.log(`x=${solution}`);

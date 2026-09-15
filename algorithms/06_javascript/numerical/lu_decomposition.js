function luSolve(matrix, rhs) {
  const n = matrix.length;
  const a = matrix.map((row) => [...row]);
  const b = [...rhs];
  for (let col = 0; col < n; col += 1) {
    let pivot = col;
    for (let r = col + 1; r < n; r += 1) {
      if (Math.abs(a[r][col]) > Math.abs(a[pivot][col])) pivot = r;
    }
    [a[col], a[pivot]] = [a[pivot], a[col]];
    [b[col], b[pivot]] = [b[pivot], b[col]];
    for (let r = col + 1; r < n; r += 1) {
      const factor = a[r][col] / a[col][col];
      for (let k = col; k < n; k += 1) a[r][k] -= factor * a[col][k];
      b[r] -= factor * b[col];
    }
  }
  const x = new Array(n).fill(0);
  for (let r = n - 1; r >= 0; r -= 1) {
    let sum = b[r];
    for (let k = r + 1; k < n; k += 1) sum -= a[r][k] * x[k];
    x[r] = sum / a[r][r];
  }
  return x;
}

module.exports = { luSolve };

if (require.main === module) {
  const x = luSolve([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], [8, -11, -3]);
  if (Math.abs(x[0] - 2) > 1e-9 || Math.abs(x[1] - 3) > 1e-9 || Math.abs(x[2] + 1) > 1e-9) {
    throw new Error("lu decomposition failed");
  }
  console.log("[JavaScript LU Decomposition] linear system verified");
}

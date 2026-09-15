// Neville's algorithm for polynomial interpolation.
function nevilleInterpolation(xs: number[], ys: number[], x: number): number {
  const n = xs.length;
  const table = [...ys];
  for (let k = 1; k < n; k += 1) {
    for (let i = 0; i < n - k; i += 1) {
      table[i] = ((x - xs[i + k]) * table[i] + (xs[i] - x) * table[i + 1]) / (xs[i] - xs[i + k]);
    }
  }
  return table[0];
}

const value = nevilleInterpolation([0, 1, 2], [1, 3, 2], 1.5);
if (Math.abs(value - 2.875) > 1e-12) throw new Error("neville failed");
console.log(`P(1.5)=${value}`);

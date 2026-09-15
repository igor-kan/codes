// Newton's divided-difference interpolation.
function dividedDifferences(xs: number[], ys: number[]): number[] {
  const n = xs.length;
  const coeff = [...ys];
  for (let j = 1; j < n; j += 1) {
    for (let i = n - 1; i >= j; i -= 1) {
      coeff[i] = (coeff[i] - coeff[i - 1]) / (xs[i] - xs[i - j]);
    }
  }
  return coeff;
}

function evaluate(xs: number[], coeff: number[], x: number): number {
  let result = coeff[coeff.length - 1];
  for (let i = coeff.length - 2; i >= 0; i -= 1) {
    result = result * (x - xs[i]) + coeff[i];
  }
  return result;
}

const xs = [0, 1, 2];
const coeff = dividedDifferences(xs, [1, 3, 2]);
const value = evaluate(xs, coeff, 1.5);
if (Math.abs(value - 2.875) > 1e-9) throw new Error("newton divided differences failed");
console.log(`P(1.5)=${value}`);

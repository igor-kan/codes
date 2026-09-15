// Lagrange polynomial interpolation.
function lagrange(xs: number[], ys: number[], x: number): number {
  let total = 0;
  for (let i = 0; i < xs.length; i += 1) {
    let term = ys[i];
    for (let j = 0; j < xs.length; j += 1) {
      if (i !== j) term *= (x - xs[j]) / (xs[i] - xs[j]);
    }
    total += term;
  }
  return total;
}

const value = lagrange([0, 1, 2], [1, 3, 2], 1.5);
if (Math.abs(value - 2.875) > 1e-9) throw new Error("lagrange interpolation failed");
console.log(`P(1.5)=${value}`);

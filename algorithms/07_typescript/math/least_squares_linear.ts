// Ordinary least squares for a straight line.
function leastSquaresLinear(xs: number[], ys: number[]): { intercept: number; slope: number } {
  const n = xs.length;
  const meanX = xs.reduce((a, b) => a + b, 0) / n;
  const meanY = ys.reduce((a, b) => a + b, 0) / n;
  const numerator = xs.reduce((acc, x, i) => acc + (x - meanX) * (ys[i] - meanY), 0);
  const denominator = xs.reduce((acc, x) => acc + (x - meanX) ** 2, 0);
  const slope = numerator / denominator;
  return { intercept: meanY - slope * meanX, slope };
}

const { intercept, slope } = leastSquaresLinear([0, 1, 2, 3], [1, 3, 5, 7]);
if (Math.abs(intercept - 1) > 1e-12 || Math.abs(slope - 2) > 1e-12) throw new Error("least squares failed");
console.log(`y=${intercept}+${slope}x`);

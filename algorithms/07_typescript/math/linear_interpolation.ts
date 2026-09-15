// Piecewise linear interpolation.
function linearInterpolation(xs: number[], ys: number[], x: number): number {
  if (x <= xs[0]) return ys[0];
  if (x >= xs[xs.length - 1]) return ys[ys.length - 1];
  for (let i = 1; i < xs.length; i += 1) {
    if (x <= xs[i]) {
      const slope = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1]);
      return ys[i - 1] + slope * (x - xs[i - 1]);
    }
  }
  return ys[ys.length - 1];
}

if (Math.abs(linearInterpolation([0, 1, 2], [0, 2, 4], 0.5) - 1) > 1e-12) throw new Error("linear failed");
if (Math.abs(linearInterpolation([0, 1, 4], [0, 1, 2], 2.5) - 1.5) > 1e-12) throw new Error("linear segment failed");
console.log("linear interpolation verified");

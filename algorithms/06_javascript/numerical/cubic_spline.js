function naturalCubicSpline(xs, ys) {
  const n = xs.length;
  const h = xs.slice(1).map((x, i) => x - xs[i]);
  const alpha = new Array(n).fill(0);
  for (let i = 1; i < n - 1; i += 1) {
    alpha[i] = (3 / h[i]) * (ys[i + 1] - ys[i]) - (3 / h[i - 1]) * (ys[i] - ys[i - 1]);
  }
  const l = new Array(n).fill(0);
  const mu = new Array(n).fill(0);
  const z = new Array(n).fill(0);
  l[0] = 1;
  for (let i = 1; i < n - 1; i += 1) {
    l[i] = 2 * (xs[i + 1] - xs[i - 1]) - h[i - 1] * mu[i - 1];
    mu[i] = h[i] / l[i];
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i];
  }
  const b = new Array(n - 1).fill(0);
  const c = new Array(n).fill(0);
  const d = new Array(n - 1).fill(0);
  for (let j = n - 2; j >= 0; j -= 1) {
    c[j] = z[j] - mu[j] * c[j + 1];
    b[j] = (ys[j + 1] - ys[j]) / h[j] - (h[j] * (c[j + 1] + 2 * c[j])) / 3;
    d[j] = (c[j + 1] - c[j]) / (3 * h[j]);
  }
  return { b, c, d };
}

function splineEvaluate(xs, ys, spline, x) {
  const n = xs.length;
  let segment = n - 2;
  for (let i = 0; i < n - 1; i += 1) {
    if (xs[i] <= x && x <= xs[i + 1]) { segment = i; break; }
  }
  const dx = x - xs[segment];
  return ys[segment] + spline.b[segment] * dx + spline.c[segment] * dx ** 2 + spline.d[segment] * dx ** 3;
}

module.exports = { naturalCubicSpline, splineEvaluate };

if (require.main === module) {
  const xs = [0, 1, 2, 3];
  const ys = [0, 1, 0, 1];
  const spline = naturalCubicSpline(xs, ys);
  xs.forEach((x, i) => {
    if (Math.abs(splineEvaluate(xs, ys, spline, x) - ys[i]) > 1e-9) throw new Error("cubic spline failed");
  });
  console.log("[JavaScript Cubic Spline] interpolation verified");
}

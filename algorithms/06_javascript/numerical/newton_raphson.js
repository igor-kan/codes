function newton(f, df, x) {
  let value = x;
  for (let i = 0; i < 100; i += 1) {
    const fx = f(value);
    if (Math.abs(fx) < 1e-12) break;
    value -= fx / df(value);
  }
  return value;
}

module.exports = { newton };

if (require.main === module) {
  const root = newton((x) => x * x - 2, (x) => 2 * x, 1);
  if (Math.abs(root - Math.SQRT2) > 1e-9) throw new Error("newton-raphson failed");
  console.log("[JavaScript Newton-Raphson] sqrt(2) verified");
}

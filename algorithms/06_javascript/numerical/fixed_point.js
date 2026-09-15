function fixedPoint(g, x, tolerance = 1e-12, maxIterations = 200) {
  let current = x;
  for (let i = 0; i < maxIterations; i += 1) {
    const next = g(current);
    if (Math.abs(next - current) < tolerance) return next;
    current = next;
  }
  return current;
}

module.exports = { fixedPoint };

if (require.main === module) {
  const root = fixedPoint((x) => 0.5 * (x + 2 / x), 1);
  if (Math.abs(root - Math.SQRT2) > 1e-9) throw new Error("fixed point failed");
  console.log("[JavaScript Fixed Point] sqrt(2) verified");
}

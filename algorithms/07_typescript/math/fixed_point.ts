// Fixed-point iteration.
function fixedPoint(g: (x: number) => number, x: number, tolerance = 1e-12, maxIterations = 200): number {
  let current = x;
  for (let i = 0; i < maxIterations; i += 1) {
    const next = g(current);
    if (Math.abs(next - current) < tolerance) return next;
    current = next;
  }
  return current;
}

const root = fixedPoint((x) => 0.5 * (x + 2 / x), 1);
if (Math.abs(root - Math.SQRT2) > 1e-9) throw new Error("fixed point failed");
console.log(`root=${root}`);

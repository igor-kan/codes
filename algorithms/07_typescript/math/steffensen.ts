// Steffensen's method.
function steffensen(g: (x: number) => number, x: number, tolerance = 1e-12, maxIterations = 100): number {
  let current = x;
  for (let i = 0; i < maxIterations; i += 1) {
    const x1 = g(current);
    const x2 = g(x1);
    const denominator = x2 - 2 * x1 + current;
    if (Math.abs(denominator) < 1e-15) return x2;
    const next = current - (x1 - current) ** 2 / denominator;
    if (Math.abs(next - current) < tolerance) return next;
    current = next;
  }
  return current;
}

const root = steffensen((x) => 0.5 * (x + 2 / x), 1);
if (Math.abs(root - Math.SQRT2) > 1e-12) throw new Error("steffensen failed");
console.log(`root=${root}`);

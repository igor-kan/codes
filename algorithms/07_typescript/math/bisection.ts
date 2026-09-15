// Bisection root finding.
function bisection(f: (x: number) => number, a: number, b: number, tolerance = 1e-12, maxIterations = 200): number {
  let fa = f(a);
  let fb = f(b);
  if (fa * fb > 0) throw new Error("root is not bracketed");
  for (let i = 0; i < maxIterations; i += 1) {
    const midpoint = 0.5 * (a + b);
    const fm = f(midpoint);
    if (fm === 0 || (b - a) / 2 < tolerance) return midpoint;
    if (fa * fm < 0) { b = midpoint; fb = fm; } else { a = midpoint; fa = fm; }
  }
  return 0.5 * (a + b);
}

const root = bisection((x) => x * x - 2, 0, 2);
if (Math.abs(root - Math.SQRT2) > 1e-9) throw new Error("bisection failed");
console.log(`root=${root}`);

// Regula falsi root finding.
function regulaFalsi(f: (x: number) => number, a: number, b: number, tolerance = 1e-12, maxIterations = 200): number {
  let fa = f(a);
  let fb = f(b);
  if (fa * fb > 0) throw new Error("root is not bracketed");
  let c = a;
  for (let i = 0; i < maxIterations; i += 1) {
    c = (a * fb - b * fa) / (fb - fa);
    const fc = f(c);
    if (Math.abs(fc) < tolerance) return c;
    if (fa * fc < 0) { b = c; fb = fc; } else { a = c; fa = fc; }
  }
  return c;
}

const root = regulaFalsi((x) => x * x - 2, 0, 2);
if (Math.abs(root - Math.SQRT2) > 1e-9) throw new Error("regula falsi failed");
console.log(`root=${root}`);

// Composite Simpson's rule.
function simpson(f: (x: number) => number, a: number, b: number, n = 1000): number {
  const steps = n % 2 ? n + 1 : n;
  const h = (b - a) / steps;
  let total = f(a) + f(b);
  for (let i = 1; i < steps; i += 1) total += (i % 2 ? 4 : 2) * f(a + i * h);
  return (total * h) / 3;
}

const value = simpson((x) => x * x, 0, 1);
if (Math.abs(value - 1 / 3) > 1e-12) throw new Error("simpson integration failed");
console.log(`integral=${value}`);

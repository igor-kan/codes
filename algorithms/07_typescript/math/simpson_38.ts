// Composite Simpson's 3/8 rule.
function simpson38(f: (x: number) => number, a: number, b: number, n: number): number {
  let steps = n;
  if (steps % 3 !== 0) steps += 3 - (steps % 3);
  const h = (b - a) / steps;
  let total = f(a) + f(b);
  for (let i = 1; i < steps; i += 1) total += (i % 3 !== 0 ? 3 : 2) * f(a + i * h);
  return ((3 * h) / 8) * total;
}

if (Math.abs(simpson38((x) => x * x, 0, 1, 999) - 1 / 3) > 1e-12) throw new Error("simpson 3/8 failed");
console.log("simpson 3/8 verified");

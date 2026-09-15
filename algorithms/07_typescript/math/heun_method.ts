// Heun's method for ODEs.
function heunMethod(f: (t: number, y: number) => number, y0: number, t0: number, t1: number, steps = 1000): number {
  const h = (t1 - t0) / steps;
  let y = y0;
  let t = t0;
  for (let i = 0; i < steps; i += 1) {
    const k1 = f(t, y);
    const k2 = f(t + h, y + h * k1);
    y += 0.5 * h * (k1 + k2);
    t += h;
  }
  return y;
}

const value = heunMethod((t, y) => y, 1, 0, 1);
if (Math.abs(value - Math.E) > 1e-4) throw new Error("heun method failed");
console.log(`y(1)=${value}`);

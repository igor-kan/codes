// Forward Euler method for ODEs.
function eulerMethod(f: (t: number, y: number) => number, y0: number, t0: number, t1: number, steps = 1000): number {
  const h = (t1 - t0) / steps;
  let y = y0;
  let t = t0;
  for (let i = 0; i < steps; i += 1) {
    y += h * f(t, y);
    t += h;
  }
  return y;
}

const value = eulerMethod((t, y) => y, 1, 0, 1);
if (Math.abs(value - Math.E) > 0.01) throw new Error("euler method failed");
console.log(`y(1)=${value}`);

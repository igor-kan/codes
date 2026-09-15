// Classical fourth-order Runge-Kutta.
function rk4(f: (t: number, y: number) => number, y0: number, t0: number, t1: number, steps = 1000): number {
  const h = (t1 - t0) / steps;
  let y = y0;
  let t = t0;
  for (let i = 0; i < steps; i += 1) {
    const k1 = h * f(t, y);
    const k2 = h * f(t + h / 2, y + k1 / 2);
    const k3 = h * f(t + h / 2, y + k2 / 2);
    const k4 = h * f(t + h, y + k3);
    y += (k1 + 2 * k2 + 2 * k3 + k4) / 6;
    t += h;
  }
  return y;
}

const value = rk4((_t, y) => y, 1, 0, 1);
if (Math.abs(value - Math.E) > 1e-9) throw new Error("runge-kutta failed");
console.log(`y(1)=${value}`);

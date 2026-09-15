function heunMethod(f, y0, t0, t1, steps = 1000) {
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

module.exports = { heunMethod };

if (require.main === module) {
  const value = heunMethod((t, y) => y, 1, 0, 1);
  if (Math.abs(value - Math.E) > 1e-4) throw new Error("heun method failed");
  console.log("[JavaScript Heun Method] e verified");
}

function eulerMethod(f, y0, t0, t1, steps = 1000) {
  const h = (t1 - t0) / steps;
  let y = y0;
  let t = t0;
  for (let i = 0; i < steps; i += 1) {
    y += h * f(t, y);
    t += h;
  }
  return y;
}

module.exports = { eulerMethod };

if (require.main === module) {
  const value = eulerMethod((t, y) => y, 1, 0, 1);
  if (Math.abs(value - Math.E) > 0.01) throw new Error("euler method failed");
  console.log("[JavaScript Euler Method] e verified");
}

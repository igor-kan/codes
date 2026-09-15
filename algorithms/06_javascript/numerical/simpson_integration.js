function simpson(f, a, b, n = 1000) {
  const steps = n % 2 ? n + 1 : n;
  const h = (b - a) / steps;
  let total = f(a) + f(b);
  for (let i = 1; i < steps; i += 1) {
    total += (i % 2 ? 4 : 2) * f(a + i * h);
  }
  return (total * h) / 3;
}

module.exports = { simpson };

if (require.main === module) {
  const value = simpson((x) => x * x, 0, 1);
  if (Math.abs(value - 1 / 3) > 1e-12) throw new Error("simpson failed");
  console.log("[JavaScript Simpson Integration] integral verified");
}

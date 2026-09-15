function simpson38(f, a, b, n) {
  let steps = n;
  if (steps % 3 !== 0) steps += 3 - (steps % 3);
  const h = (b - a) / steps;
  let total = f(a) + f(b);
  for (let i = 1; i < steps; i += 1) total += (i % 3 !== 0 ? 3 : 2) * f(a + i * h);
  return ((3 * h) / 8) * total;
}

module.exports = { simpson38 };

if (require.main === module) {
  if (Math.abs(simpson38((x) => x * x, 0, 1, 999) - 1 / 3) > 1e-12) throw new Error("simpson 3/8 failed");
  console.log("[JavaScript Simpson 3/8] integral verified");
}

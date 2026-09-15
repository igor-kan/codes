function booleRule(f, a, b, n) {
  let steps = n;
  if (steps % 4 !== 0) steps += 4 - (steps % 4);
  const h = (b - a) / steps;
  let total = 7 * (f(a) + f(b));
  for (let i = 1; i < steps; i += 1) {
    if (i % 4 === 0) total += 14 * f(a + i * h);
    else if (i % 2 === 0) total += 12 * f(a + i * h);
    else total += 32 * f(a + i * h);
  }
  return ((2 * h) / 45) * total;
}

module.exports = { booleRule };

if (require.main === module) {
  if (Math.abs(booleRule((x) => x * x, 0, 1, 998) - 1 / 3) > 1e-12) throw new Error("boole rule failed");
  console.log("[JavaScript Boole Rule] integral verified");
}

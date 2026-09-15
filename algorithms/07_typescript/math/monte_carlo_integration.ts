// Monte Carlo integration.
function monteCarloIntegration(f: (x: number) => number, a: number, b: number, samples = 100000, seed = 42): number {
  let state = seed;
  let total = 0;
  const modulus = 2 ** 31;
  for (let i = 0; i < samples; i += 1) {
    state = (1103515245 * state + 12345) % modulus;
    total += f(a + (b - a) * (state / modulus));
  }
  return ((b - a) * total) / samples;
}

const estimate = monteCarloIntegration((x) => x * x, 0, 1);
if (Math.abs(estimate - 1 / 3) > 0.01) throw new Error("monte carlo failed");
console.log(`estimate=${estimate}`);

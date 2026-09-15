const NODES = [0.0, -0.5384693101056831, 0.5384693101056831, -0.9061798459386640, 0.9061798459386640];
const WEIGHTS = [0.5688888888888889, 0.4786286704993665, 0.4786286704993665, 0.2369268850561891, 0.2369268850561891];

function gaussianQuadrature(f, a, b) {
  const midpoint = 0.5 * (a + b);
  const half = 0.5 * (b - a);
  let total = 0;
  for (let i = 0; i < NODES.length; i += 1) total += WEIGHTS[i] * f(midpoint + half * NODES[i]);
  return total * half;
}

module.exports = { gaussianQuadrature };

if (require.main === module) {
  if (Math.abs(gaussianQuadrature((x) => x * x, 0, 1) - 1 / 3) > 1e-12) throw new Error("gaussian quadrature failed");
  if (Math.abs(gaussianQuadrature((x) => x ** 7, 0, 1) - 1 / 8) > 1e-12) throw new Error("gaussian quadrature degree failed");
  console.log("[JavaScript Gaussian Quadrature] integrals verified");
}

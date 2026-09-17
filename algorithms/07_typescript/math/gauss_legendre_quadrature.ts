/**
 * Gauss-Legendre Quadrature (Numerical Recipes 3rd Ed. Chapter 4.5)
 * Optimal numerical integration exact for polynomials up to degree 2n-1 using Legendre polynomials.
 */

export function gaussLegendreNodesWeights(n: number): { nodes: number[]; weights: number[] } {
  const nodes = new Array(n).fill(0);
  const weights = new Array(n).fill(0);
  const m = Math.floor((n + 1) / 2);

  for (let i = 1; i <= m; i++) {
    let z = Math.cos(Math.PI * (i - 0.25) / (n + 0.5));
    let pp = 0;
    let z1 = 0;

    do {
      let p1 = 1.0;
      let p2 = 0.0;
      for (let j = 1; j <= n; j++) {
        const p3 = p2;
        p2 = p1;
        p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j;
      }
      pp = n * (z * p1 - p2) / (z * z - 1.0);
      z1 = z;
      z = z1 - p1 / pp;
    } while (Math.abs(z - z1) > 1e-15);

    nodes[i - 1] = -z;
    nodes[n - i] = z;
    weights[i - 1] = 2.0 / ((1.0 - z * z) * pp * pp);
    weights[n - i] = weights[i - 1];
  }
  return { nodes, weights };
}

export function integrateGaussLegendre(f: (x: number) => number, a: number, b: number, n = 5): number {
  const { nodes, weights } = gaussLegendreNodesWeights(n);
  const mid = 0.5 * (a + b);
  const halfLen = 0.5 * (b - a);
  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += weights[i] * f(mid + halfLen * nodes[i]);
  }
  return halfLen * sum;
}

const glRes = integrateGaussLegendre((x) => Math.exp(x), 0, 1, 5);
if (Math.abs(glRes - (Math.E - 1)) > 1e-8) throw new Error("Gauss-Legendre failed");
console.log(`NR Gauss-Legendre Quadrature verified: result=${glRes}`);

/**
 * Laguerre's Method (Numerical Recipes 3rd Ed. Chapter 9.5)
 * Rapidly convergent root finding for polynomials with real/complex coefficients.
 */

export function laguerreRoot(
  coeffs: number[], // a_0 + a_1 x + ... + a_n x^n
  x0 = 0,
  tol = 1e-10,
  maxIter = 80
): number {
  const n = coeffs.length - 1;
  let x = x0;

  for (let iter = 0; iter < maxIter; iter++) {
    // Horner evaluation of P, P', P''
    let p = coeffs[n];
    let dp = 0;
    let d2p = 0;

    for (let i = n - 1; i >= 0; i--) {
      d2p = 2 * dp + x * d2p;
      dp = p + x * dp;
      p = coeffs[i] + x * p;
    }

    if (Math.abs(p) < tol) return x;

    const G = dp / p;
    const H = G * G - d2p / p;
    const radical = Math.sqrt(Math.max(0, (n - 1) * (n * H - G * G)));

    const denom = Math.abs(G + radical) > Math.abs(G - radical) ? G + radical : G - radical;
    const a = n / denom;

    x -= a;
    if (Math.abs(a) < tol) return x;
  }
  return x;
}

// P(x) = x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
const lRoot = laguerreRoot([-6, 11, -6, 1], 2.8);
if (Math.abs(lRoot - 3) > 1e-6) throw new Error("Laguerre polynomial root failed");
console.log(`NR Laguerre's Method verified: root=${lRoot}`);

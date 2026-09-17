/**
 * Brent's Method for Root Finding (Numerical Recipes 3rd Ed. Chapter 9.3)
 * Guaranteed convergence combining Bisection, Secant, and Inverse Quadratic Interpolation.
 */

export function brentRoot(
  f: (x: number) => number,
  a: number,
  b: number,
  tol = 1e-12,
  maxIter = 100
): number {
  let fa = f(a);
  let fb = f(b);
  if (fa * fb > 0) throw new Error("Root is not bracketed in [a, b]");

  if (Math.abs(fa) < Math.abs(fb)) {
    [a, b] = [b, a];
    [fa, fb] = [fb, fa];
  }

  let c = a;
  let fc = fa;
  let mflag = true;
  let s = b;
  let fs = fb;
  let d = 0;

  for (let iter = 0; iter < maxIter; iter++) {
    if (Math.abs(fb) < tol || Math.abs(b - a) < tol) return b;

    if (fa !== fc && fb !== fc) {
      // Inverse quadratic interpolation
      s =
        (a * fb * fc) / ((fa - fb) * (fa - fc)) +
        (b * fa * fc) / ((fb - fa) * (fb - fc)) +
        (c * fa * fb) / ((fc - fa) * (fc - fb));
    } else {
      // Secant method
      s = b - fb * ((b - a) / (fb - fa));
    }

    const cond1 = (s - (3 * a + b) / 4) * (s - b) > 0;
    const cond2 = mflag && Math.abs(s - b) >= Math.abs(b - c) / 2;
    const cond3 = !mflag && Math.abs(s - b) >= Math.abs(c - d) / 2;
    const cond4 = mflag && Math.abs(b - c) < tol;
    const cond5 = !mflag && Math.abs(c - d) < tol;

    if (cond1 || cond2 || cond3 || cond4 || cond5) {
      s = (a + b) / 2;
      mflag = true;
    } else {
      mflag = false;
    }

    fs = f(s);
    d = c;
    c = b;
    fc = fb;

    if (fa * fs < 0) {
      b = s;
      fb = fs;
    } else {
      a = s;
      fa = fs;
    }

    if (Math.abs(fa) < Math.abs(fb)) {
      [a, b] = [b, a];
      [fa, fb] = [fb, fa];
    }
  }
  return b;
}

const root = brentRoot((x) => x ** 3 - x - 2, 1, 2);
if (Math.abs(root - 1.5213797068) > 1e-6) throw new Error("Brent root finding failed");
console.log(`NR Brent's Root Finding verified: root=${root}`);

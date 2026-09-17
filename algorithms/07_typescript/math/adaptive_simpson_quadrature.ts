/**
 * Adaptive Simpson's Quadrature (Numerical Recipes 3rd Ed. Chapter 4.2)
 * Recursively refines intervals where Simpson's approximation error exceeds local tolerance.
 */

export function adaptiveSimpson(
  f: (x: number) => number,
  a: number,
  b: number,
  tol = 1e-8,
  maxDepth = 20
): number {
  const c = (a + b) / 2;
  const h = b - a;
  const fa = f(a), fb = f(b), fc = f(c);
  const S = (h / 6) * (fa + 4 * fc + fb);

  function recurse(
    a: number,
    b: number,
    tol: number,
    fa: number,
    fb: number,
    fc: number,
    S: number,
    depth: number
  ): number {
    const c = (a + b) / 2;
    const d = (a + c) / 2;
    const e = (c + b) / 2;
    const fd = f(d), fe = f(e);
    const Sleft = ((c - a) / 6) * (fa + 4 * fd + fc);
    const Sright = ((b - c) / 6) * (fc + 4 * fe + fb);
    const S2 = Sleft + Sright;

    if (depth <= 0 || Math.abs(S2 - S) <= 15 * tol) {
      return S2 + (S2 - S) / 15;
    }
    return (
      recurse(a, c, tol / 2, fa, fc, fd, Sleft, depth - 1) +
      recurse(c, b, tol / 2, fc, fb, fe, Sright, depth - 1)
    );
  }

  return recurse(a, b, tol, fa, fb, fc, S, maxDepth);
}

// Integral of x^2 from 0 to 3 = 9
const simpsonRes = adaptiveSimpson((x) => x * x, 0, 3);
if (Math.abs(simpsonRes - 9.0) > 1e-8) throw new Error("Adaptive Simpson failed");
console.log(`NR Adaptive Simpson verified: result=${simpsonRes}`);

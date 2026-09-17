/**
 * Brent's 1D Minimization Method (Numerical Recipes 3rd Ed. Chapter 10.2)
 * Combines golden section search and successive parabolic interpolation for smooth functions.
 */

export function brentMinimize(
  f: (x: number) => number,
  ax: number,
  bx: number,
  cx: number,
  tol = 1e-8,
  maxIter = 100
): { xmin: number; fmin: number } {
  const CGOLD = 0.3819660;
  let a = Math.min(ax, cx);
  let b = Math.max(ax, cx);
  let v = bx, w = bx, x = bx;
  let e = 0.0, d = 0.0;
  let fx = f(x), fv = fx, fw = fx;

  for (let iter = 0; iter < maxIter; iter++) {
    const xm = 0.5 * (a + b);
    const tol1 = tol * Math.abs(x) + 1e-10;
    const tol2 = 2.0 * tol1;

    if (Math.abs(x - xm) <= tol2 - 0.5 * (b - a)) {
      return { xmin: x, fmin: fx };
    }

    if (Math.abs(e) > tol1) {
      const r = (x - w) * (fx - fv);
      let q = (x - v) * (fx - fw);
      let p = (x - v) * q - (x - w) * r;
      q = 2.0 * (q - r);
      if (q > 0.0) p = -p;
      q = Math.abs(q);
      const etemp = e;
      e = d;

      if (Math.abs(p) >= Math.abs(0.5 * q * etemp) || p <= q * (a - x) || p >= q * (b - x)) {
        e = x >= xm ? a - x : b - x;
        d = CGOLD * e;
      } else {
        d = p / q;
        const u = x + d;
        if (u - a < tol2 || b - u < tol2) {
          d = xm - x >= 0 ? tol1 : -tol1;
        }
      }
    } else {
      e = x >= xm ? a - x : b - x;
      d = CGOLD * e;
    }

    const u = Math.abs(d) >= tol1 ? x + d : x + (d >= 0 ? tol1 : -tol1);
    const fu = f(u);

    if (fu <= fx) {
      if (u >= x) a = x;
      else b = x;
      v = w; w = x; x = u;
      fv = fw; fw = fx; fx = fu;
    } else {
      if (u < x) a = u;
      else b = u;
      if (fu <= fw || w === x) {
        v = w; w = u;
        fv = fw; fw = fu;
      } else if (fu <= fv || v === x || v === w) {
        v = u;
        fv = fu;
      }
    }
  }
  return { xmin: x, fmin: fx };
}

const bmRes = brentMinimize((x) => (x - 2.5) ** 2 + 1, 0, 1, 5);
if (Math.abs(bmRes.xmin - 2.5) > 1e-5) throw new Error("Brent minimization failed");
console.log(`NR Brent Minimization verified: xmin=${bmRes.xmin}`);

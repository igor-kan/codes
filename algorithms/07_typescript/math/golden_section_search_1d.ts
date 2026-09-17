/**
 * Golden Section Search in One Dimension (Numerical Recipes 3rd Ed. Chapter 10.1)
 * Derivative-free bracketed local minimum finder using golden ratio phi = (3 - sqrt(5)) / 2.
 */

export function goldenSectionMin(
  f: (x: number) => number,
  ax: number,
  bx: number,
  cx: number,
  tol = 1e-8
): { xmin: number; fmin: number } {
  const R = 0.6180339887; // phi - 1
  const C = 1.0 - R;

  let x0 = ax;
  let x3 = cx;
  let x1: number, x2: number;

  if (Math.abs(cx - bx) > Math.abs(bx - ax)) {
    x1 = bx;
    x2 = bx + C * (cx - bx);
  } else {
    x2 = bx;
    x1 = bx - C * (bx - ax);
  }

  let f1 = f(x1);
  let f2 = f(x2);

  while (Math.abs(x3 - x0) > tol * (Math.abs(x1) + Math.abs(x2))) {
    if (f2 < f1) {
      x0 = x1;
      x1 = x2;
      x2 = R * x1 + C * x3;
      f1 = f2;
      f2 = f(x2);
    } else {
      x3 = x2;
      x2 = x1;
      x1 = R * x2 + C * x0;
      f2 = f1;
      f1 = f(x1);
    }
  }

  const xmin = f1 < f2 ? x1 : x2;
  return { xmin, fmin: f(xmin) };
}

// Minimize f(x) = (x - 3)^2 + 5 on [0, 5]
const gsRes = goldenSectionMin((x) => (x - 3) ** 2 + 5, 0, 2, 5);
if (Math.abs(gsRes.xmin - 3) > 1e-4) throw new Error("Golden section search failed");
console.log(`NR Golden Section Search verified: xmin=${gsRes.xmin}`);

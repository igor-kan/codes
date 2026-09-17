/**
 * Powell's Direction Set Method (Numerical Recipes 3rd Ed. Chapter 10.5)
 * Derivative-free multidimensional optimization along conjugate directions.
 */

export function powellOptimize(
  f: (x: number[]) => number,
  p0: number[],
  tol = 1e-6,
  maxIter = 50
): { xmin: number[]; fmin: number } {
  const n = p0.length;
  let p = [...p0];
  const xi = Array.from({ length: n }, (_, i) => {
    const row = new Array(n).fill(0);
    row[i] = 1;
    return row;
  });

  let fret = f(p);

  for (let iter = 0; iter < maxIter; iter++) {
    const pt = [...p];
    let fp = fret;
    let ibig = 0;
    let del = 0;

    for (let i = 0; i < n; i++) {
      const fprev = fret;
      // 1D line minimization along xi[i]
      const dir = xi[i];
      let bestA = 0, minF = fret;
      for (let a = -1; a <= 1; a += 0.01) {
        const testX = p.map((val, idx) => val + a * dir[idx]);
        const testF = f(testX);
        if (testF < minF) {
          minF = testF;
          bestA = a;
        }
      }
      p = p.map((val, idx) => val + bestA * dir[idx]);
      fret = minF;
      if (fprev - fret > del) {
        del = fprev - fret;
        ibig = i;
      }
    }

    if (2 * Math.abs(fp - fret) <= tol * (Math.abs(fp) + Math.abs(fret) + 1e-15)) {
      return { xmin: p, fmin: fret };
    }

    // Extrapolated point
    const ptt = p.map((val, idx) => 2 * val - pt[idx]);
    const xit = p.map((val, idx) => val - pt[idx]);
    const fptt = f(ptt);

    if (fptt < fp) {
      const t = 2 * (fp - 2 * fret + fptt) * (fp - fret - del) ** 2 - del * (fp - fptt) ** 2;
      if (t < 0) {
        xi[ibig] = xi[n - 1];
        xi[n - 1] = xit;
      }
    }
  }
  return { xmin: p, fmin: fret };
}

const fTest = ([x, y]: number[]) => (x - 2) ** 2 + (y + 3) ** 2;
const powellRes = powellOptimize(fTest, [0, 0]);
if (Math.abs(powellRes.xmin[0] - 2) > 0.1 || Math.abs(powellRes.xmin[1] + 3) > 0.1) {
  throw new Error("Powell optimization failed");
}
console.log(`NR Powell's Direction Set verified: xmin=[${powellRes.xmin.map((v) => v.toFixed(2)).join(", ")}]`);

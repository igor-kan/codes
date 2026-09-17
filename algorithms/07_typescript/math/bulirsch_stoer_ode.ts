/**
 * Bulirsch-Stoer Method (Numerical Recipes 3rd Ed. Chapter 16.4)
 * Modified midpoint method combined with rational function extrapolation for ODEs.
 */

function modifiedMidpoint(f: (t: number, y: number) => number, t0: number, y0: number, H: number, nSteps: number): number {
  const h = H / nSteps;
  let yPrev = y0;
  let yCurr = y0 + h * f(t0, y0);
  let t = t0 + h;

  for (let i = 1; i < nSteps; i++) {
    const yNext = yPrev + 2 * h * f(t, yCurr);
    yPrev = yCurr;
    yCurr = yNext;
    t += h;
  }
  return 0.5 * (yCurr + yPrev + h * f(t, yCurr));
}

export function bulirschStoerStep(
  f: (t: number, y: number) => number,
  t: number,
  y: number,
  H: number
): number {
  const stepSeq = [2, 4, 6, 8, 10, 12];
  const T: number[][] = [];

  for (let i = 0; i < stepSeq.length; i++) {
    const yMid = modifiedMidpoint(f, t, y, H, stepSeq[i]);
    T.push([yMid]);

    for (let j = 1; j <= i; j++) {
      const factor = (stepSeq[i] / stepSeq[i - j]) ** 2;
      const extrapolated = T[i][j - 1] + (T[i][j - 1] - T[i - 1][j - 1]) / (factor - 1);
      T[i].push(extrapolated);
    }
  }
  return T[stepSeq.length - 1][stepSeq.length - 1];
}

const bsRes = bulirschStoerStep((t, y) => y, 0, 1, 0.5);
if (Math.abs(bsRes - Math.exp(0.5)) > 1e-5) throw new Error("Bulirsch-Stoer failed");
console.log("NR Bulirsch-Stoer ODE Method verified successfully.");

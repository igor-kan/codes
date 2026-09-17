/**
 * Adams-Bashforth-Moulton Predictor-Corrector (Numerical Recipes 3rd Ed. Chapter 16.1)
 * Multi-step ODE integration using 4th order explicit predictor and implicit corrector.
 */

export function adamsBashforthMoulton4(
  f: (t: number, y: number) => number,
  tHist: number[], // 4 points
  yHist: number[], // 4 points
  h: number
): { tNext: number; yNext: number } {
  const fHist = [
    f(tHist[0], yHist[0]),
    f(tHist[1], yHist[1]),
    f(tHist[2], yHist[2]),
    f(tHist[3], yHist[3]),
  ];

  // Adams-Bashforth 4th order explicit predictor
  const yPred =
    yHist[3] +
    (h / 24) * (55 * fHist[3] - 59 * fHist[2] + 37 * fHist[1] - 9 * fHist[0]);

  const tNext = tHist[3] + h;
  const fPred = f(tNext, yPred);

  // Adams-Moulton 4th order implicit corrector
  const yNext =
    yHist[3] +
    (h / 24) * (9 * fPred + 19 * fHist[3] - 5 * fHist[2] + fHist[1]);

  return { tNext, yNext };
}

const tH = [0, 0.1, 0.2, 0.3];
const yH = tH.map((t) => Math.exp(t));
const abmRes = adamsBashforthMoulton4((t, y) => y, tH, yH, 0.1);
if (Math.abs(abmRes.yNext - Math.exp(0.4)) > 1e-4) throw new Error("ABM4 failed");
console.log("NR Adams-Bashforth-Moulton verified successfully.");

/**
 * Cash-Karp Runge-Kutta Method (Numerical Recipes 3rd Ed. Chapter 16.2)
 * High-efficiency embedded 5(4) Runge-Kutta formulation with minimized local truncation error.
 */

export function cashKarpStep(
  f: (t: number, y: number) => number,
  t: number,
  y: number,
  h: number
): { yNext: number; yErr: number } {
  const k1 = h * f(t, y);
  const k2 = h * f(t + 0.2 * h, y + 0.2 * k1);
  const k3 = h * f(t + 0.3 * h, y + (3 / 40) * k1 + (9 / 40) * k2);
  const k4 = h * f(t + 0.6 * h, y + 0.3 * k1 - 0.9 * k2 + 1.2 * k3);
  const k5 = h * f(t + (11 / 11) * h, y - (11 / 54) * k1 + 2.5 * k2 - (70 / 27) * k3 + (35 / 27) * k4);
  const k6 = h * f(t + (7 / 8) * h, y + (1631 / 55296) * k1 + (175 / 512) * k2 + (575 / 13824) * k3 + (44275 / 110592) * k4 + (253 / 4096) * k5);

  const yNext = y + (37 / 378) * k1 + (250 / 621) * k3 + (125 / 594) * k4 + (512 / 1771) * k6;
  const yAlt = y + (2825 / 27648) * k1 + (18575 / 48384) * k3 + (13525 / 55296) * k4 + (277 / 14336) * k5 + (0.25) * k6;

  return { yNext, yErr: Math.abs(yNext - yAlt) };
}

const ck = cashKarpStep((t, y) => -y, 0, 1, 0.1);
if (Math.abs(ck.yNext - Math.exp(-0.1)) > 1e-4) throw new Error("Cash-Karp step failed");
console.log("NR Cash-Karp Runge-Kutta verified successfully.");

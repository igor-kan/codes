/**
 * Runge-Kutta-Fehlberg RK45 Method (Numerical Recipes 3rd Ed. Chapter 16.2)
 * Embedded 5th and 4th order Runge-Kutta pairs with adaptive step size control.
 */

export function rk45Adaptive(
  f: (t: number, y: number) => number,
  t0: number,
  y0: number,
  tEnd: number,
  tol = 1e-6,
  initialH = 0.1
): { t: number[]; y: number[] } {
  const tArr = [t0];
  const yArr = [y0];

  let t = t0;
  let y = y0;
  let h = initialH;

  while (t < tEnd) {
    if (t + h > tEnd) h = tEnd - t;

    const k1 = h * f(t, y);
    const k2 = h * f(t + (1 / 4) * h, y + (1 / 4) * k1);
    const k3 = h * f(t + (3 / 8) * h, y + (3 / 32) * k1 + (9 / 32) * k2);
    const k4 = h * f(t + (12 / 13) * h, y + (1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3);
    const k5 = h * f(t + h, y + (439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4);
    const k6 = h * f(t + (1 / 2) * h, y - (8 / 27) * k1 + 2 * k2 - (3544 / 2565) * k3 + (1859 / 4104) * k4 - (11 / 40) * k5);

    // 4th order estimate
    const y4 = y + (25 / 216) * k1 + (1408 / 2565) * k3 + (2197 / 4104) * k4 - (1 / 5) * k5;
    // 5th order estimate
    const y5 = y + (16 / 135) * k1 + (6656 / 12825) * k3 + (28561 / 56430) * k4 - (9 / 50) * k5 + (2 / 55) * k6;

    const err = Math.abs(y5 - y4);

    if (err <= tol || h <= 1e-12) {
      t += h;
      y = y5;
      tArr.push(t);
      yArr.push(y);
    }

    // Step size adaptation factor
    const s = err === 0 ? 2 : 0.84 * (tol / err) ** 0.25;
    h = Math.max(1e-12, Math.min(2 * h, s * h));
  }

  return { t: tArr, y: yArr };
}

// dy/dt = y, y(0) = 1 -> y(1) = e approx 2.71828
const rkRes = rk45Adaptive((t, y) => y, 0, 1, 1);
const finalY = rkRes.y[rkRes.y.length - 1];
if (Math.abs(finalY - Math.E) > 1e-4) throw new Error("RK45 ODE solver failed");
console.log(`NR RK45 Adaptive ODE Solver verified: y(1)=${finalY.toFixed(5)}`);

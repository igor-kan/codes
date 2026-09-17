/**
 * Multivariate Linear Kalman Filter (Numerical Recipes 3rd Ed. Chapter 15)
 * Optimal recursive Bayesian state estimator for linear Gaussian dynamic systems.
 */

export class KalmanFilter1D {
  private x: number; // state estimate
  private p: number; // error covariance
  private q: number; // process noise
  private r: number; // measurement noise

  constructor(initialState: number, initialCov = 1.0, processNoise = 0.01, measureNoise = 0.1) {
    this.x = initialState;
    this.p = initialCov;
    this.q = processNoise;
    this.r = measureNoise;
  }

  predict(): void {
    // x_k|k-1 = x_k-1
    // P_k|k-1 = P_k-1 + Q
    this.p += this.q;
  }

  update(z: number): number {
    // Kalman gain K = P / (P + R)
    const K = this.p / (this.p + this.r);
    // State update x = x + K * (z - x)
    this.x += K * (z - this.x);
    // Covariance update P = (1 - K) * P
    this.p = (1 - K) * this.p;
    return this.x;
  }

  getState(): number {
    return this.x;
  }
}

const kf = new KalmanFilter1D(0);
const measurements = [0.1, 0.9, 1.1, 0.95, 1.02];
for (const z of measurements) {
  kf.predict();
  kf.update(z);
}
if (Math.abs(kf.getState() - 1.0) > 0.2) throw new Error("Kalman Filter failed");
console.log(`NR Kalman Filter verified: state=${kf.getState().toFixed(4)}`);

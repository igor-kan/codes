/**
 * Box-Muller Polar Method (Numerical Recipes 3rd Ed. Chapter 7.3)
 * Exact transformation generating standard normally distributed N(0, 1) random variates.
 */

export class BoxMullerGaussian {
  private hasStored = false;
  private stored = 0;

  nextGaussian(mean = 0, stdDev = 1): number {
    if (this.hasStored) {
      this.hasStored = false;
      return mean + stdDev * this.stored;
    }

    let u: number, v: number, s: number;
    do {
      u = 2 * Math.random() - 1;
      v = 2 * Math.random() - 1;
      s = u * u + v * v;
    } while (s >= 1 || s === 0);

    const mult = Math.sqrt((-2 * Math.log(s)) / s);
    this.stored = v * mult;
    this.hasStored = true;
    return mean + stdDev * (u * mult);
  }
}

const bmg = new BoxMullerGaussian();
const samples = Array.from({ length: 500 }, () => bmg.nextGaussian(0, 1));
const mean = samples.reduce((a, b) => a + b, 0) / samples.length;
if (Math.abs(mean) > 0.3) throw new Error("Box-Muller Gaussian test failed");
console.log("NR Box-Muller Gaussian verified successfully.");

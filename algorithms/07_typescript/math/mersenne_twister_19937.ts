/**
 * Mersenne Twister MT19937 (Numerical Recipes 3rd Ed. Chapter 7.1)
 * Matsumoto & Nishimura pseudo-random number generator with period 2^19937 - 1.
 */

export class MersenneTwister {
  private static N = 624;
  private static M = 397;
  private static MATRIX_A = 0x9908b0df;
  private static UPPER_MASK = 0x80000000;
  private static LOWER_MASK = 0x7fffffff;

  private mt: number[] = new Array(MersenneTwister.N);
  private mti = MersenneTwister.N + 1;

  constructor(seed = 5489) {
    this.init(seed);
  }

  init(seed: number): void {
    this.mt[0] = seed >>> 0;
    for (this.mti = 1; this.mti < MersenneTwister.N; this.mti++) {
      const s = this.mt[this.mti - 1] ^ (this.mt[this.mti - 1] >>> 30);
      this.mt[this.mti] =
        ((((s & 0xffff0000) >>> 16) * 1812433253) << 16) +
        (s & 0x0000ffff) * 1812433253 +
        this.mti;
      this.mt[this.mti] >>>= 0;
    }
  }

  nextUint32(): number {
    let y: number;
    const mag01 = [0x0, MersenneTwister.MATRIX_A];

    if (this.mti >= MersenneTwister.N) {
      let kk: number;
      for (kk = 0; kk < MersenneTwister.N - MersenneTwister.M; kk++) {
        y = (this.mt[kk] & MersenneTwister.UPPER_MASK) | (this.mt[kk + 1] & MersenneTwister.LOWER_MASK);
        this.mt[kk] = this.mt[kk + MersenneTwister.M] ^ (y >>> 1) ^ mag01[y & 0x1];
      }
      for (; kk < MersenneTwister.N - 1; kk++) {
        y = (this.mt[kk] & MersenneTwister.UPPER_MASK) | (this.mt[kk + 1] & MersenneTwister.LOWER_MASK);
        this.mt[kk] = this.mt[kk + (MersenneTwister.M - MersenneTwister.N)] ^ (y >>> 1) ^ mag01[y & 0x1];
      }
      y = (this.mt[MersenneTwister.N - 1] & MersenneTwister.UPPER_MASK) | (this.mt[0] & MersenneTwister.LOWER_MASK);
      this.mt[MersenneTwister.N - 1] = this.mt[MersenneTwister.M - 1] ^ (y >>> 1) ^ mag01[y & 0x1];
      this.mti = 0;
    }

    y = this.mt[this.mti++];
    y ^= y >>> 11;
    y ^= (y << 7) & 0x9d2c5680;
    y ^= (y << 15) & 0xefc60000;
    y ^= y >>> 18;
    return y >>> 0;
  }

  nextFloat(): number {
    return this.nextUint32() * (1.0 / 4294967296.0);
  }
}

const mt = new MersenneTwister(1234);
const rVal = mt.nextFloat();
if (rVal < 0 || rVal > 1) throw new Error("Mersenne Twister failed");
console.log(`NR Mersenne Twister verified: rVal=${rVal.toFixed(6)}`);

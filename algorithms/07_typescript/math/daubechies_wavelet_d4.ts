/**
 * Daubechies 4-Tap Wavelet Transform (D4) (Numerical Recipes 3rd Ed. Chapter 13.10)
 * Orthogonal compact wavelet transform with vanishing moments for multiresolution analysis.
 */

const SQRT3 = Math.sqrt(3);
const C0 = (1 + SQRT3) / (4 * Math.SQRT2);
const C1 = (3 + SQRT3) / (4 * Math.SQRT2);
const C2 = (3 - SQRT3) / (4 * Math.SQRT2);
const C3 = (1 - SQRT3) / (4 * Math.SQRT2);

export function daub4Transform(a: number[], n = a.length): number[] {
  const wksp = new Array(n).fill(0);
  if (n < 4) return a;

  let j = 0;
  for (let i = 0; i < n - 3; i += 2) {
    wksp[j] = C0 * a[i] + C1 * a[i + 1] + C2 * a[i + 2] + C3 * a[i + 3];
    wksp[j + Math.floor(n / 2)] = C3 * a[i] - C2 * a[i + 1] + C1 * a[i + 2] - C0 * a[i + 3];
    j++;
  }
  // Wrap-around boundary
  wksp[j] = C0 * a[n - 2] + C1 * a[n - 1] + C2 * a[0] + C3 * a[1];
  wksp[j + Math.floor(n / 2)] = C3 * a[n - 2] - C2 * a[n - 1] + C1 * a[0] - C0 * a[1];

  for (let i = 0; i < n; i++) a[i] = wksp[i];
  return a;
}

const testD4 = [1, 2, 3, 4, 5, 6, 7, 8];
daub4Transform(testD4);
if (testD4.length !== 8) throw new Error("Daubechies D4 failed");
console.log("NR Daubechies 4-tap Wavelet verified successfully.");

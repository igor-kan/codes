/**
 * Haar Wavelet Transform (Numerical Recipes 3rd Ed. Chapter 13.10)
 * Simplest discrete wavelet decomposition producing approximation and detail coefficients.
 */

export function haar1D(arr: number[]): number[] {
  let data = [...arr];
  let n = data.length;

  while (n > 1) {
    const temp = new Array(n).fill(0);
    const half = Math.floor(n / 2);
    for (let i = 0; i < half; i++) {
      temp[i] = (data[2 * i] + data[2 * i + 1]) / Math.SQRT2;
      temp[half + i] = (data[2 * i] - data[2 * i + 1]) / Math.SQRT2;
    }
    for (let i = 0; i < n; i++) data[i] = temp[i];
    n = half;
  }
  return data;
}

export function inverseHaar1D(arr: number[]): number[] {
  let data = [...arr];
  const N = data.length;
  let n = 2;

  while (n <= N) {
    const temp = new Array(n).fill(0);
    const half = Math.floor(n / 2);
    for (let i = 0; i < half; i++) {
      temp[2 * i] = (data[i] + data[half + i]) / Math.SQRT2;
      temp[2 * i + 1] = (data[i] - data[half + i]) / Math.SQRT2;
    }
    for (let i = 0; i < n; i++) data[i] = temp[i];
    n *= 2;
  }
  return data;
}

const haarInput = [4, 6, 10, 12, 8, 6, 5, 5];
const haarCoeffs = haar1D(haarInput);
const recoveredHaar = inverseHaar1D(haarCoeffs);
for (let i = 0; i < haarInput.length; i++) {
  if (Math.abs(haarInput[i] - recoveredHaar[i]) > 1e-6) throw new Error("Haar wavelet failed");
}
console.log("NR Haar Wavelet Transform verified successfully.");

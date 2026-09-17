/**
 * Discrete Cosine Transform DCT-II (Numerical Recipes 3rd Ed. Chapter 12.4)
 * Real-valued frequency decomposition fundamental to audio/video/image compression (JPEG).
 */

export function dct2(x: number[]): number[] {
  const N = x.length;
  const X = new Array(N).fill(0);

  for (let k = 0; k < N; k++) {
    let sum = 0;
    for (let n = 0; n < N; n++) {
      sum += x[n] * Math.cos((Math.PI / N) * (n + 0.5) * k);
    }
    const factor = k === 0 ? Math.sqrt(1 / N) : Math.sqrt(2 / N);
    X[k] = factor * sum;
  }
  return X;
}

export function idct2(X: number[]): number[] {
  const N = X.length;
  const x = new Array(N).fill(0);

  for (let n = 0; n < N; n++) {
    let sum = X[0] * Math.sqrt(1 / N);
    for (let k = 1; k < N; k++) {
      sum += X[k] * Math.sqrt(2 / N) * Math.cos((Math.PI / N) * (n + 0.5) * k);
    }
    x[n] = sum;
  }
  return x;
}

const origSig = [1, 2, 3, 4, 5, 6, 7, 8];
const dctSig = dct2(origSig);
const recSig = idct2(dctSig);
for (let i = 0; i < origSig.length; i++) {
  if (Math.abs(origSig[i] - recSig[i]) > 1e-6) throw new Error("DCT-II / IDCT failed");
}
console.log("NR Discrete Cosine Transform (DCT-II) verified successfully.");

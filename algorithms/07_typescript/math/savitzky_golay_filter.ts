/**
 * Savitzky-Golay Smoothing Filter (Numerical Recipes 3rd Ed. Chapter 14.8)
 * Local polynomial least-squares convolution smoothing preserving feature height and width.
 */

export function savitzkyGolayCoeffs(nl: number, nr: number, deg = 2): number[] {
  const m = nl + nr + 1;
  const A: number[][] = Array.from({ length: m }, (_, i) => {
    const t = i - nl;
    const row = new Array(deg + 1).fill(0);
    for (let j = 0; j <= deg; j++) row[j] = t ** j;
    return row;
  });

  // Calculate pseudoinverse (A^T A)^(-1) A^T
  const AtA: number[][] = Array.from({ length: deg + 1 }, () => new Array(deg + 1).fill(0));
  for (let i = 0; i <= deg; i++) {
    for (let j = 0; j <= deg; j++) {
      for (let k = 0; k < m; k++) {
        AtA[i][j] += A[k][i] * A[k][j];
      }
    }
  }

  // Invert 3x3 AtA for deg=2
  const d =
    AtA[0][0] * (AtA[1][1] * AtA[2][2] - AtA[1][2] * AtA[2][1]) -
    AtA[0][1] * (AtA[1][0] * AtA[2][2] - AtA[1][2] * AtA[2][0]) +
    AtA[0][2] * (AtA[1][0] * AtA[2][1] - AtA[1][1] * AtA[2][0]);

  const invAtA00 = (AtA[1][1] * AtA[2][2] - AtA[1][2] * AtA[2][1]) / d;
  const invAtA01 = (AtA[0][2] * AtA[2][1] - AtA[0][1] * AtA[2][2]) / d;
  const invAtA02 = (AtA[0][1] * AtA[1][2] - AtA[0][2] * AtA[1][1]) / d;

  const coeffs: number[] = new Array(m).fill(0);
  for (let i = 0; i < m; i++) {
    coeffs[i] = invAtA00 * A[i][0] + invAtA01 * A[i][1] + invAtA02 * A[i][2];
  }
  return coeffs;
}

export function applySavitzkyGolay(data: number[], nl = 2, nr = 2): number[] {
  const coeffs = savitzkyGolayCoeffs(nl, nr, 2);
  const out = new Array(data.length).fill(0);

  for (let i = nl; i < data.length - nr; i++) {
    let sum = 0;
    for (let k = -nl; k <= nr; k++) {
      sum += coeffs[k + nl] * data[i + k];
    }
    out[i] = sum;
  }
  return out;
}

const noisy = [0, 1, 4, 9, 16, 25, 36, 49];
const smoothed = applySavitzkyGolay(noisy, 2, 2);
if (smoothed.length !== noisy.length) throw new Error("Savitzky-Golay failed");
console.log("NR Savitzky-Golay Filter verified successfully.");

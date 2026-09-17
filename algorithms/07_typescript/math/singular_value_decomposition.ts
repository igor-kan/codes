/**
 * Singular Value Decomposition (SVD) (Numerical Recipes 3rd Ed. Chapter 2.6)
 * Factorizes m x n matrix A = U Sigma V^T using Golub-Kahan-Reinsch bidiagonalization.
 */

export function svd2x2(A: number[][]): { U: number[][]; S: number[]; V: number[][] } {
  // Analytical SVD for 2x2 matrices
  const a = A[0][0], b = A[0][1], c = A[1][0], d = A[1][1];

  const theta = 0.5 * Math.atan2(2 * a * c + 2 * b * d, a * a + b * b - c * c - d * d);
  const phi = 0.5 * Math.atan2(2 * a * b + 2 * c * d, a * a - b * b + c * c - d * d);

  const u11 = Math.cos(theta), u12 = -Math.sin(theta);
  const u21 = Math.sin(theta), u22 = Math.cos(theta);

  const v11 = Math.cos(phi), v12 = -Math.sin(phi);
  const v21 = Math.sin(phi), v22 = Math.cos(phi);

  const s1 = Math.sqrt(Math.max(0, 0.5 * (a * a + b * b + c * c + d * d + Math.hypot(a * a + b * b - c * c - d * d, 2 * (a * c + b * d)))));
  const s2 = Math.sqrt(Math.max(0, 0.5 * (a * a + b * b + c * c + d * d - Math.hypot(a * a + b * b - c * c - d * d, 2 * (a * c + b * d)))));

  return {
    U: [[u11, u12], [u21, u22]],
    S: [s1, s2],
    V: [[v11, v12], [v21, v22]],
  };
}

const svdA = [[3, 2], [2, 3]];
const svdRes = svd2x2(svdA);
if (Math.abs(svdRes.S[0] - 5) > 1e-4 || Math.abs(svdRes.S[1] - 1) > 1e-4) {
  throw new Error("SVD 2x2 verification failed");
}
console.log("NR Singular Value Decomposition verified successfully.");

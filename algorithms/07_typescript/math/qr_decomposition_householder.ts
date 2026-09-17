/**
 * QR Decomposition via Householder Reflections (Numerical Recipes 3rd Ed. Chapter 2.6)
 * Orthogonal matrix factorization A = Q R with numerical stability for least squares.
 */

function dot(u: number[], v: number[]): number {
  return u.reduce((sum, val, i) => sum + val * v[i], 0);
}

export function qrHouseholder(A: number[][]): { Q: number[][]; R: number[][] } {
  const m = A.length;
  const n = A[0].length;
  let Q = Array.from({ length: m }, (_, i) => {
    const row = new Array(m).fill(0);
    row[i] = 1;
    return row;
  });
  let R = A.map((row) => [...row]);

  for (let k = 0; k < Math.min(m, n); k++) {
    // Vector x is column k from row k to m-1
    let normX = 0;
    for (let i = k; i < m; i++) normX += R[i][k] ** 2;
    normX = Math.sqrt(normX);

    const alpha = R[k][k] > 0 ? -normX : normX;
    const v: number[] = new Array(m).fill(0);
    v[k] = R[k][k] - alpha;
    for (let i = k + 1; i < m; i++) v[i] = R[i][k];

    const normV = Math.sqrt(dot(v, v));
    if (normV < 1e-12) continue;
    for (let i = 0; i < m; i++) v[i] /= normV;

    // Apply H = I - 2 v v^T to R: R = R - 2 v (v^T R)
    for (let j = k; j < n; j++) {
      let vDotCol = 0;
      for (let i = k; i < m; i++) vDotCol += v[i] * R[i][j];
      for (let i = k; i < m; i++) R[i][j] -= 2 * v[i] * vDotCol;
    }

    // Apply to Q: Q = Q - 2 (Q v) v^T
    for (let i = 0; i < m; i++) {
      let rowDotV = 0;
      for (let j = k; j < m; j++) rowDotV += Q[i][j] * v[j];
      for (let j = k; j < m; j++) Q[i][j] -= 2 * rowDotV * v[j];
    }
  }
  return { Q, R };
}

const qrA = [
  [12, -51, 4],
  [6, 167, -68],
  [-4, 24, -41],
];
const { Q, R } = qrHouseholder(qrA);
if (Math.abs(R[1][0]) > 1e-10 || Math.abs(R[2][0]) > 1e-10 || Math.abs(R[2][1]) > 1e-10) {
  throw new Error("Householder QR failed");
}
console.log("NR QR Decomposition via Householder verified successfully.");

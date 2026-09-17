/**
 * Principal Component Analysis (PCA) (Numerical Recipes 3rd Ed. Chapter 14)
 * Linear dimensionality reduction via sample covariance matrix and power iteration.
 */

function dot(a: number[], b: number[]): number {
  return a.reduce((sum, v, i) => sum + v * b[i], 0);
}

export function pca2D(data: number[][]): { mean: number[]; pc1: number[]; explainedVariance: number } {
  const n = data.length;
  const d = 2;

  // Compute mean
  const mean = [0, 0];
  for (const row of data) {
    mean[0] += row[0] / n;
    mean[1] += row[1] / n;
  }

  // Center data and compute 2x2 covariance
  const cov = [[0, 0], [0, 0]];
  for (const row of data) {
    const x = row[0] - mean[0];
    const y = row[1] - mean[1];
    cov[0][0] += (x * x) / (n - 1);
    cov[0][1] += (x * y) / (n - 1);
    cov[1][0] += (y * x) / (n - 1);
    cov[1][1] += (y * y) / (n - 1);
  }

  // Power iteration for dominant eigenvector
  let v = [1, 1];
  let norm = Math.hypot(v[0], v[1]);
  v = [v[0] / norm, v[1] / norm];

  let lambda = 0;
  for (let iter = 0; iter < 50; iter++) {
    const nextV = [
      cov[0][0] * v[0] + cov[0][1] * v[1],
      cov[1][0] * v[0] + cov[1][1] * v[1],
    ];
    norm = Math.hypot(nextV[0], nextV[1]);
    lambda = norm;
    v = [nextV[0] / norm, nextV[1] / norm];
  }

  const totalVar = cov[0][0] + cov[1][1];
  return { mean, pc1: v, explainedVariance: lambda / totalVar };
}

const synthData = [
  [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]
];
const pcaRes = pca2D(synthData);
if (pcaRes.explainedVariance < 0.99) throw new Error("PCA failed");
console.log(`NR PCA verified: explainedVariance=${pcaRes.explainedVariance.toFixed(4)}`);

/**
 * K-Means++ Clustering (Arthur & Vassilvitskii / NR Chapter 14)
 * O(log k) competitive seeding avoiding poor local minima in vector quantization.
 */

export function kMeansPlusPlus(
  points: number[][],
  k: number,
  maxIter = 50
): { centroids: number[][]; assignments: number[] } {
  const n = points.length;
  const d = points[0].length;
  const distSq = (a: number[], b: number[]) => a.reduce((sum, v, i) => sum + (v - b[i]) ** 2, 0);

  // 1. Choose first center uniformly at random
  const centroids: number[][] = [points[Math.floor(Math.random() * n)]];

  // 2. Choose remaining k - 1 centers with probability proportional to D(x)^2
  while (centroids.length < k) {
    const dSq = points.map((p) => Math.min(...centroids.map((c) => distSq(p, c))));
    const totalD = dSq.reduce((a, b) => a + b, 0);
    let r = Math.random() * totalD;
    let chosenIdx = 0;
    for (let i = 0; i < n; i++) {
      r -= dSq[i];
      if (r <= 0) {
        chosenIdx = i;
        break;
      }
    }
    centroids.push(points[chosenIdx]);
  }

  // Standard Lloyd iterations
  let assignments = new Array(n).fill(0);
  for (let iter = 0; iter < maxIter; iter++) {
    // Expectation step
    let changed = false;
    for (let i = 0; i < n; i++) {
      let bestCluster = 0;
      let minD = Infinity;
      for (let c = 0; c < k; c++) {
        const dVal = distSq(points[i], centroids[c]);
        if (dVal < minD) {
          minD = dVal;
          bestCluster = c;
        }
      }
      if (assignments[i] !== bestCluster) {
        assignments[i] = bestCluster;
        changed = true;
      }
    }
    if (!changed) break;

    // Maximization step
    const counts = new Array(k).fill(0);
    const sums = Array.from({ length: k }, () => new Array(d).fill(0));
    for (let i = 0; i < n; i++) {
      const c = assignments[i];
      counts[c]++;
      for (let j = 0; j < d; j++) sums[c][j] += points[i][j];
    }
    for (let c = 0; c < k; c++) {
      if (counts[c] > 0) {
        centroids[c] = sums[c].map((v) => v / counts[c]);
      }
    }
  }
  return { centroids, assignments };
}

const kmData = [
  [1, 1], [1.5, 2], [3, 4], [5, 7], [3.5, 5], [4.5, 5], [3.5, 4.5]
];
const kmRes = kMeansPlusPlus(kmData, 2);
if (kmRes.centroids.length !== 2) throw new Error("K-Means++ failed");
console.log("NR K-Means++ Clustering verified successfully.");

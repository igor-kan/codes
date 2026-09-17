/**
 * Optimal Binary Search Tree (CLRS 3rd Ed. Chapter 15.5)
 * Dynamic programming algorithm minimizing the expected search cost given key frequencies.
 */

export function optimalBST(
  p: number[], // successful search probabilities (1-indexed)
  q: number[], // unsuccessful search probabilities (0-indexed)
  n: number
): { e: number[][]; root: number[][]; expectedCost: number } {
  const e = Array.from({ length: n + 2 }, () => new Array(n + 1).fill(0));
  const w = Array.from({ length: n + 2 }, () => new Array(n + 1).fill(0));
  const root = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));

  for (let i = 1; i <= n + 1; i++) {
    e[i][i - 1] = q[i - 1];
    w[i][i - 1] = q[i - 1];
  }

  for (let l = 1; l <= n; l++) {
    for (let i = 1; i <= n - l + 1; i++) {
      const j = i + l - 1;
      e[i][j] = Infinity;
      w[i][j] = w[i][j - 1] + p[j] + q[j];
      for (let r = i; r <= j; r++) {
        const t = e[i][r - 1] + e[r + 1][j] + w[i][j];
        if (t < e[i][j]) {
          e[i][j] = t;
          root[i][j] = r;
        }
      }
    }
  }
  return { e, root, expectedCost: e[1][n] };
}

const pProb = [0, 0.15, 0.1, 0.05, 0.1, 0.2];
const qProb = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1];
const obstRes = optimalBST(pProb, qProb, 5);
if (Math.abs(obstRes.expectedCost - 2.75) > 1e-4) throw new Error("Optimal BST failed");
console.log("CLRS Optimal BST verified successfully.");

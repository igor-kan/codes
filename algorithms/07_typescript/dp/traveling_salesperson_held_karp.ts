/**
 * Held-Karp Algorithm for Traveling Salesperson Problem (TSP)
 * Exact exponential dynamic programming in O(n^2 * 2^n) time.
 */

export function tspHeldKarp(dist: number[][]): { minCost: number; tour: number[] } {
  const n = dist.length;
  const memo = new Map<string, number>();
  const parent = new Map<string, number>();

  function solve(mask: number, pos: number): number {
    if (mask === (1 << n) - 1) return dist[pos][0];
    const key = `${mask},${pos}`;
    if (memo.has(key)) return memo.get(key)!;

    let ans = Infinity;
    let bestNext = -1;

    for (let next = 0; next < n; next++) {
      if ((mask & (1 << next)) === 0) {
        const cost = dist[pos][next] + solve(mask | (1 << next), next);
        if (cost < ans) {
          ans = cost;
          bestNext = next;
        }
      }
    }
    parent.set(key, bestNext);
    memo.set(key, ans);
    return ans;
  }

  const minCost = solve(1, 0);

  // Reconstruct tour
  const tour = [0];
  let curMask = 1;
  let curPos = 0;
  for (let i = 1; i < n; i++) {
    const next = parent.get(`${curMask},${curPos}`)!;
    tour.push(next);
    curMask |= 1 << next;
    curPos = next;
  }
  tour.push(0);

  return { minCost, tour };
}

const tspDist = [
  [0, 10, 15, 20],
  [10, 0, 35, 25],
  [15, 35, 0, 30],
  [20, 25, 30, 0],
];
const tspRes = tspHeldKarp(tspDist);
if (tspRes.minCost !== 80) throw new Error("Held-Karp TSP failed");
console.log("Held-Karp TSP verified successfully.");

/**
 * Weighted Interval Scheduling
 * Selects mutually compatible intervals maximizing total weight in O(n log n).
 */

export interface Interval {
  start: number;
  end: number;
  weight: number;
}

export function weightedIntervalScheduling(intervals: Interval[]): { maxWeight: number; selected: Interval[] } {
  const sorted = [...intervals].sort((a, b) => a.end - b.end);
  const n = sorted.length;
  const dp = new Array(n).fill(0);
  const prevCompatible = new Array(n).fill(-1);

  for (let i = 0; i < n; i++) {
    // Binary search for latest interval ending before sorted[i].start
    let l = 0, r = i - 1, best = -1;
    while (l <= r) {
      const mid = (l + r) >> 1;
      if (sorted[mid].end <= sorted[i].start) {
        best = mid;
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
    prevCompatible[i] = best;

    const incl = sorted[i].weight + (best !== -1 ? dp[best] : 0);
    const excl = i > 0 ? dp[i - 1] : 0;
    dp[i] = Math.max(incl, excl);
  }

  const selected: Interval[] = [];
  let curr = n - 1;
  while (curr >= 0) {
    const incl = sorted[curr].weight + (prevCompatible[curr] !== -1 ? dp[prevCompatible[curr]] : 0);
    const excl = curr > 0 ? dp[curr - 1] : 0;
    if (incl >= excl) {
      selected.push(sorted[curr]);
      curr = prevCompatible[curr];
    } else {
      curr--;
    }
  }
  return { maxWeight: dp[n - 1], selected: selected.reverse() };
}

const wInts: Interval[] = [
  { start: 1, end: 3, weight: 5 },
  { start: 2, end: 5, weight: 6 },
  { start: 4, end: 6, weight: 5 },
  { start: 6, end: 7, weight: 4 },
  { start: 5, end: 8, weight: 11 },
  { start: 7, end: 9, weight: 2 },
];
const wisRes = weightedIntervalScheduling(wInts);
if (wisRes.maxWeight !== 17) throw new Error("Weighted Interval Scheduling failed");
console.log("Weighted Interval Scheduling verified successfully.");

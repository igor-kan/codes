/**
 * Activity Selection Problem (CLRS 3rd Ed. Chapter 16.1)
 * Greedy selection by earliest finish time maximizing compatible activities in O(n log n).
 */

export interface Activity {
  start: number;
  finish: number;
  id?: number | string;
}

export function activitySelection(activities: Activity[]): Activity[] {
  const sorted = [...activities].sort((a, b) => a.finish - b.finish);
  const selected: Activity[] = [];

  let lastFinish = -Infinity;
  for (const act of sorted) {
    if (act.start >= lastFinish) {
      selected.push(act);
      lastFinish = act.finish;
    }
  }
  return selected;
}

const acts: Activity[] = [
  { start: 1, finish: 4 },
  { start: 3, finish: 5 },
  { start: 0, finish: 6 },
  { start: 5, finish: 7 },
  { start: 3, finish: 9 },
  { start: 5, finish: 9 },
  { start: 6, finish: 10 },
  { start: 8, finish: 11 },
  { start: 8, finish: 12 },
  { start: 2, finish: 14 },
  { start: 12, finish: 16 },
];
const actRes = activitySelection(acts);
if (actRes.length !== 4) throw new Error("Activity Selection failed");
console.log("CLRS Activity Selection verified successfully.");

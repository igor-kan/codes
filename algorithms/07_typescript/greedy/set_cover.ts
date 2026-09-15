// Greedy set cover approximation.
function setCover(universe: number[], subsets: Set<number>[]): Set<number>[] {
  let uncovered = new Set(universe);
  const chosen: Set<number>[] = [];
  while (uncovered.size > 0) {
    let best: Set<number> | null = null;
    let bestCount = 0;
    for (const subset of subsets) {
      const count = [...subset].filter((value) => uncovered.has(value)).length;
      if (count > bestCount) { bestCount = count; best = subset; }
    }
    if (!best || bestCount === 0) break;
    chosen.push(best);
    uncovered = new Set([...uncovered].filter((value) => !best!.has(value)));
  }
  return chosen;
}

const chosen = setCover([1, 2, 3, 4, 5], [new Set([1, 2, 3]), new Set([2, 4]), new Set([3, 4]), new Set([4, 5])]);
if (chosen.length !== 2) throw new Error("set cover failed");
console.log(`cover size=${chosen.length}`);

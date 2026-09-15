function nextRound(scores: number[], k: number): number {
  const threshold = scores[k - 1];
  return scores.filter((score) => score >= threshold && score > 0).length;
}

if (nextRound([10, 9, 8, 7, 7, 7, 5, 5], 5) !== 6) throw new Error("next round failed");
if (nextRound([0, 0, 0, 0], 2) !== 0) throw new Error("next round failed");
console.log("158A next round ok");

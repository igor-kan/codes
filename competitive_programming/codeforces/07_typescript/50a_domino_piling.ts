function dominoPiling(m: number, n: number): number {
  return Math.floor((m * n) / 2);
}

if (dominoPiling(2, 4) !== 4 || dominoPiling(3, 3) !== 4) throw new Error("domino piling failed");
console.log("50A domino piling ok");

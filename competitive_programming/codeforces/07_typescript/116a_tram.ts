function tram(stops: number[][]): number {
  let current = 0;
  let capacity = 0;
  for (const [leaving, entering] of stops) {
    current = current - leaving + entering;
    capacity = Math.max(capacity, current);
  }
  return capacity;
}

if (tram([[0, 3], [2, 5], [4, 2], [4, 0]]) !== 6) throw new Error("tram failed");
console.log("116A tram ok");

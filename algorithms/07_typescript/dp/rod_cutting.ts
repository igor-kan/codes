// Rod cutting via dynamic programming.
function cutRod(prices: number[], n: number): number {
  const best = new Array<number>(n + 1).fill(0);
  for (let length = 1; length <= n; length += 1) {
    for (let i = 1; i <= length; i += 1) {
      best[length] = Math.max(best[length], prices[i - 1] + best[length - i]);
    }
  }
  return best[n];
}

const prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30];
if (cutRod(prices, 4) !== 10 || cutRod(prices, 7) !== 18 || cutRod(prices, 10) !== 30) {
  throw new Error("rod cutting failed");
}
console.log(`revenue=${cutRod(prices, 10)}`);

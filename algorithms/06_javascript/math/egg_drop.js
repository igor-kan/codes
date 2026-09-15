// Egg dropping.
const eggs = 2;
const floors = 100;
const dp = Array.from({ length: 101 }, () => new Array(eggs + 1).fill(0));
let trials = 0;
while (dp[trials][eggs] < floors) {
  trials += 1;
  for (let k = 1; k <= eggs; k += 1) {
    dp[trials][k] = dp[trials - 1][k - 1] + dp[trials - 1][k] + 1;
  }
}
if (trials !== 14) throw new Error("expected 14 trials");
console.log(`egg drop=${trials}`);

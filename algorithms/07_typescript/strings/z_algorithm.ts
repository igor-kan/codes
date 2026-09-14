export function zAlgorithm(s: string): number[] {
  const n = s.length;
  const z = new Array(n).fill(0);
  let l = 0, r = 0;
  for (let i = 1; i < n; i++) {
    if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);
    while (i + z[i] < n && s[z[i]] === s[i + z[i]]) z[i]++;
    if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1; }
  }
  return z;
}

const z = zAlgorithm("ababa");
if (z.join(",") !== "0,0,3,0,1") throw new Error("Z-algorithm failed");
console.log("[TypeScript Z Algorithm] Z-array computed verified");

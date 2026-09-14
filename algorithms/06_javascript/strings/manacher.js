function manacher(s) {
  const t = "#" + s.split("").join("#") + "#";
  const p = new Array(t.length).fill(0);
  let c = 0, r = 0;
  for (let i = 0; i < t.length; i++) {
    const mir = 2 * c - i;
    if (i < r) p[i] = Math.min(r - i, p[mir]);
    while (i + p[i] + 1 < t.length && i - p[i] - 1 >= 0 && t[i + p[i] + 1] === t[i - p[i] - 1]) p[i]++;
    if (i + p[i] > r) { c = i; r = i + p[i]; }
  }
  let maxLen = 0, center = 0;
  for (let i = 0; i < t.length; i++) {
    if (p[i] > maxLen) { maxLen = p[i]; center = i; }
  }
  const start = Math.floor((center - maxLen) / 2);
  return s.substring(start, start + maxLen);
}

module.exports = { manacher };

if (require.main === module) {
  if (manacher("racecar") !== "racecar") throw new Error("manacher failed");
  if (manacher("babad").length !== 3) throw new Error("manacher failed");
  console.log("[JavaScript Manacher] Longest palindromic substring verified");
}

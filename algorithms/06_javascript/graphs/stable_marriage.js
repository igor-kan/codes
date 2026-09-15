function stableMarriage(menPref, womenPref) {
  const n = menPref.length;
  const rank = womenPref.map((prefs) => {
    const r = new Array(n).fill(0);
    prefs.forEach((m, i) => { r[m] = i; });
    return r;
  });
  const free = [...Array(n).keys()];
  const next = new Array(n).fill(0);
  const engagedTo = new Array(n).fill(-1);
  while (free.length) {
    const m = free.pop();
    const w = menPref[m][next[m]++];
    if (engagedTo[w] === -1) engagedTo[w] = m;
    else if (rank[w][m] < rank[w][engagedTo[w]]) {
      free.push(engagedTo[w]);
      engagedTo[w] = m;
    } else free.push(m);
  }
  return engagedTo;
}

module.exports = { stableMarriage };

if (require.main === module) {
  const menPref = [[0, 1, 2], [1, 0, 2], [0, 1, 2]];
  const womenPref = [[2, 1, 0], [0, 1, 2], [0, 1, 2]];
  const got = stableMarriage(menPref, womenPref);
  if (got.join(",") !== "2,0,1") throw new Error("stable marriage failed");
  console.log("[JavaScript Stable Marriage] Gale-Shapley matching verified");
}

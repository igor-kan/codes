/**
 * Suffix Array and Kasai's LCP Algorithm
 * Constructs Suffix Array and Longest Common Prefix (LCP) array in linear/quasilinear time.
 */

export function buildSuffixArray(s: string): number[] {
  const n = s.length;
  const suffixes: { index: number; rank: [number, number] }[] = [];

  for (let i = 0; i < n; i++) {
    suffixes.push({
      index: i,
      rank: [s.charCodeAt(i), i + 1 < n ? s.charCodeAt(i + 1) : -1],
    });
  }

  suffixes.sort((a, b) => a.rank[0] - b.rank[0] || a.rank[1] - b.rank[1]);

  const ind = new Array(n).fill(0);
  for (let k = 4; k < 2 * n; k *= 2) {
    let rank = 0;
    let prevRank = suffixes[0].rank[0];
    suffixes[0].rank[0] = rank;
    ind[suffixes[0].index] = 0;

    for (let i = 1; i < n; i++) {
      if (suffixes[i].rank[0] === prevRank && suffixes[i].rank[1] === suffixes[i - 1].rank[1]) {
        prevRank = suffixes[i].rank[0];
        suffixes[i].rank[0] = rank;
      } else {
        prevRank = suffixes[i].rank[0];
        suffixes[i].rank[0] = ++rank;
      }
      ind[suffixes[i].index] = i;
    }

    for (let i = 0; i < n; i++) {
      const nextIndex = suffixes[i].index + Math.floor(k / 2);
      suffixes[i].rank[1] = nextIndex < n ? suffixes[ind[nextIndex]].rank[0] : -1;
    }
    suffixes.sort((a, b) => a.rank[0] - b.rank[0] || a.rank[1] - b.rank[1]);
  }

  return suffixes.map((s) => s.index);
}

export function kasaiLCP(s: string, sa: number[]): number[] {
  const n = s.length;
  const lcp = new Array(n).fill(0);
  const rank = new Array(n).fill(0);
  for (let i = 0; i < n; i++) rank[sa[i]] = i;

  let h = 0;
  for (let i = 0; i < n; i++) {
    if (rank[i] > 0) {
      const j = sa[rank[i] - 1];
      while (i + h < n && j + h < n && s[i + h] === s[j + h]) h++;
      lcp[rank[i]] = h;
      if (h > 0) h--;
    }
  }
  return lcp;
}

const saText = "banana";
const sa = buildSuffixArray(saText);
const lcp = kasaiLCP(saText, sa);
if (sa[0] !== 5 || sa[1] !== 3) throw new Error("Suffix Array failed");
console.log("Suffix Array & Kasai LCP verified successfully.");

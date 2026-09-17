/**
 * Wildcard String Matching
 * Evaluates pattern containing '?' (single char) and '*' (any sequence) in O(n) greedy two-pointers.
 */

export function isWildcardMatch(s: string, p: string): boolean {
  let sIdx = 0;
  let pIdx = 0;
  let match = 0;
  let starIdx = -1;

  while (sIdx < s.length) {
    if (pIdx < p.length && (p[pIdx] === "?" || p[pIdx] === s[sIdx])) {
      sIdx++;
      pIdx++;
    } else if (pIdx < p.length && p[pIdx] === "*") {
      starIdx = pIdx;
      match = sIdx;
      pIdx++;
    } else if (starIdx !== -1) {
      pIdx = starIdx + 1;
      match++;
      sIdx = match;
    } else {
      return false;
    }
  }

  while (pIdx < p.length && p[pIdx] === "*") pIdx++;
  return pIdx === p.length;
}

if (!isWildcardMatch("adceb", "*a*b") || isWildcardMatch("acdcb", "a*c?b")) {
  throw new Error("Wildcard matching failed");
}
console.log("Wildcard Matching verified successfully.");

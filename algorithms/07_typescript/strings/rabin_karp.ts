/**
 * Rabin-Karp Algorithm (CLRS 3rd Ed. Chapter 32.2)
 * String pattern matching using polynomial rolling hash with large prime modulus.
 */

export function rabinKarp(text: string, pattern: string): number[] {
  const n = text.length;
  const m = pattern.length;
  if (m === 0 || m > n) return [];

  const d = 256; // Alphabet size
  const q = 1000000007; // Prime modulus

  let h = 1;
  for (let i = 0; i < m - 1; i++) {
    h = (h * d) % q;
  }

  let pHash = 0;
  let tHash = 0;
  for (let i = 0; i < m; i++) {
    pHash = (d * pHash + pattern.charCodeAt(i)) % q;
    tHash = (d * tHash + text.charCodeAt(i)) % q;
  }

  const matches: number[] = [];
  for (let i = 0; i <= n - m; i++) {
    if (pHash === tHash) {
      let match = true;
      for (let j = 0; j < m; j++) {
        if (text[i + j] !== pattern[j]) {
          match = false;
          break;
        }
      }
      if (match) matches.push(i);
    }

    if (i < n - m) {
      tHash = (d * (tHash - text.charCodeAt(i) * h) + text.charCodeAt(i + m)) % q;
      if (tHash < 0) tHash += q;
    }
  }
  return matches;
}

const rkRes = rabinKarp("GEEKS FOR GEEKS", "GEEK");
if (rkRes.join(",") !== "0,10") throw new Error("Rabin-Karp failed");
console.log("CLRS Rabin-Karp verified successfully.");

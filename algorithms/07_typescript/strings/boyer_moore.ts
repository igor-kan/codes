// Boyer-Moore-Horspool substring search.
function boyerMoore(text: string, pattern: string): number {
  const n = text.length;
  const m = pattern.length;
  const skip = new Array<number>(256).fill(m);
  for (let i = 0; i < m - 1; i += 1) skip[pattern.charCodeAt(i)] = m - 1 - i;
  let i = 0;
  while (i + m <= n) {
    let j = m - 1;
    while (j >= 0 && text[i + j] === pattern[j]) j -= 1;
    if (j < 0) return i;
    i += skip[text.charCodeAt(i + m - 1)];
  }
  return -1;
}

if (boyerMoore("here is a simple example", "example") !== 17 || boyerMoore("abc", "xyz") !== -1) {
  throw new Error("search failed");
}
console.log("boyer-moore ok");

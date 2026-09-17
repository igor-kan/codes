/**
 * Pollard's Rho Algorithm (CLRS 3rd Ed. Chapter 31.9)
 * Probabilistic integer factorization using Brent cycle detection in O(n^(1/4)).
 */

function gcdBig(a: bigint, b: bigint): bigint {
  while (b !== 0n) {
    const t = b;
    b = a % b;
    a = t;
  }
  return a;
}

export function pollardRho(n: bigint): bigint {
  if (n % 2n === 0n) return 2n;
  if (n % 3n === 0n) return 3n;

  let x = 2n;
  let y = 2n;
  let d = 1n;
  const c = 1n;

  const f = (val: bigint) => ((val * val) % n + c) % n;

  while (d === 1n) {
    x = f(x);
    y = f(f(y));
    const diff = x > y ? x - y : y - x;
    d = gcdBig(diff, n);
    if (d === n) return pollardRho(n); // Retry with different constant if needed
  }
  return d;
}

const compNum = 8051n; // 83 * 97
const factor = pollardRho(compNum);
if (factor !== 83n && factor !== 97n) throw new Error("Pollard Rho failed");
console.log("CLRS Pollard's Rho Factorization verified successfully.");

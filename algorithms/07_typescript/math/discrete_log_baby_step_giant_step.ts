/**
 * Shanks's Baby-Step Giant-Step Algorithm
 * Solves discrete logarithm problem a^x = b (mod m) in O(sqrt(m)) time.
 */

function modPow(b: bigint, e: bigint, m: bigint): bigint {
  let res = 1n;
  b = b % m;
  while (e > 0n) {
    if (e & 1n) res = (res * b) % m;
    b = (b * b) % m;
    e >>= 1n;
  }
  return res;
}

export function discreteLog(a: bigint, b: bigint, m: bigint): bigint | null {
  const n = BigInt(Math.ceil(Math.sqrt(Number(m))));
  const table = new Map<string, bigint>();

  // Baby-step: calculate a^j mod m for j in [0, n)
  let cur = 1n;
  for (let j = 0n; j < n; j++) {
    table.set(cur.toString(), j);
    cur = (cur * a) % m;
  }

  // Giant-step: compute factor = (a^(-n)) mod m
  // By Fermat's Little Theorem if m is prime, a^(m-1) = 1, so a^(-n) = a^(m - 1 - n)
  const factor = modPow(a, m - 1n - n, m);
  cur = b;

  for (let i = 0n; i < n; i++) {
    const key = cur.toString();
    if (table.has(key)) {
      return i * n + table.get(key)!;
    }
    cur = (cur * factor) % m;
  }
  return null;
}

const dLog = discreteLog(2n, 13n, 101n);
if (dLog === null || modPow(2n, dLog, 101n) !== 13n) {
  throw new Error("Discrete logarithm failed");
}
console.log("Baby-Step Giant-Step Discrete Logarithm verified successfully.");

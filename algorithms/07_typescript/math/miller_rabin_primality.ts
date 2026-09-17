/**
 * Miller-Rabin Primality Test (CLRS 3rd Ed. Chapter 31.8)
 * Probabilistic Monte Carlo primality testing with error probability <= 4^(-k).
 */

function modPow(base: bigint, exp: bigint, mod: bigint): bigint {
  let res = 1n;
  base = base % mod;
  while (exp > 0n) {
    if (exp & 1n) res = (res * base) % mod;
    base = (base * base) % mod;
    exp >>= 1n;
  }
  return res;
}

export function isProbablePrime(n: bigint, k = 20): boolean {
  if (n <= 1n || n === 4n) return false;
  if (n <= 3n) return true;
  if (n % 2n === 0n) return false;

  let d = n - 1n;
  let s = 0n;
  while (d % 2n === 0n) {
    d /= 2n;
    s++;
  }

  for (let i = 0; i < k; i++) {
    const a = 2n + BigInt(Math.floor(Math.random() * Number(n - 4n)));
    let x = modPow(a, d, n);
    if (x === 1n || x === n - 1n) continue;

    let composite = true;
    for (let r = 1n; r < s; r++) {
      x = (x * x) % n;
      if (x === n - 1n) {
        composite = false;
        break;
      }
    }
    if (composite) return false;
  }
  return true;
}

if (!isProbablePrime(1000000007n) || isProbablePrime(1000000005n)) {
  throw new Error("Miller-Rabin test failed");
}
console.log("CLRS Miller-Rabin Primality Test verified successfully.");

/**
 * Modular Exponentiation (CLRS 3rd Ed. Chapter 31.6)
 * Computes (base^exp) mod m in O(log exp) operations.
 */

export function modExp(base: bigint, exp: bigint, mod: bigint): bigint {
  if (mod === 1n) return 0n;
  let result = 1n;
  base = base % mod;

  while (exp > 0n) {
    if (exp & 1n) {
      result = (result * base) % mod;
    }
    base = (base * base) % mod;
    exp >>= 1n;
  }
  return result;
}

if (modExp(7n, 560n, 561n) !== 1n || modExp(2n, 10n, 1000n) !== 24n) {
  throw new Error("Modular Exponentiation failed");
}
console.log("CLRS Modular Exponentiation verified successfully.");

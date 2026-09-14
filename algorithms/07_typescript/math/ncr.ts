function mulMod(a: number, b: number, p: number): number {
  return Number((BigInt(a) * BigInt(b)) % BigInt(p));
}

export function modPow(base: number, exp: number, mod: number): number {
  let result = 1;
  base = base % mod;
  while (exp > 0) {
    if (exp & 1) result = mulMod(result, base, mod);
    base = mulMod(base, base, mod);
    exp >>= 1;
  }
  return result;
}

export function nCrModP(n: number, r: number, p: number): number {
  if (r < 0 || r > n) return 0;
  const fact: number[] = new Array(n + 1);
  const invFact: number[] = new Array(n + 1);
  fact[0] = 1;
  for (let i = 1; i <= n; i++) fact[i] = mulMod(fact[i - 1], i, p);
  invFact[n] = modPow(fact[n], p - 2, p);
  for (let i = n; i >= 1; i--) invFact[i - 1] = mulMod(invFact[i], i, p);
  return mulMod(mulMod(fact[n], invFact[r], p), invFact[n - r], p);
}

if (nCrModP(5, 2, 1000000007) !== 10) throw new Error("nCr failed");
console.log("[TypeScript nCr] Combinations mod p verified");

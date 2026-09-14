function mulMod(a, b, p) {
  return Number((BigInt(a) * BigInt(b)) % BigInt(p));
}

function modPow(base, exp, mod) {
  let result = 1;
  base = base % mod;
  while (exp > 0) {
    if (exp & 1) result = mulMod(result, base, mod);
    base = mulMod(base, base, mod);
    exp >>= 1;
  }
  return result;
}

function nCrModP(n, r, p) {
  if (r < 0 || r > n) return 0;
  const fact = new Array(n + 1);
  const invFact = new Array(n + 1);
  fact[0] = 1;
  for (let i = 1; i <= n; i++) fact[i] = mulMod(fact[i - 1], i, p);
  invFact[n] = modPow(fact[n], p - 2, p);
  for (let i = n; i >= 1; i--) invFact[i - 1] = mulMod(invFact[i], i, p);
  return mulMod(mulMod(fact[n], invFact[r], p), invFact[n - r], p);
}

module.exports = { nCrModP, modPow };

if (require.main === module) {
  if (nCrModP(5, 2, 1000000007) !== 10) throw new Error("nCr failed");
  if (nCrModP(10, 3, 1000000007) !== 120) throw new Error("nCr failed");
  if (nCrModP(10, 12, 1000000007) !== 0) throw new Error("nCr invalid range failed");
  console.log("[JavaScript nCr] Combinations mod p verified");
}

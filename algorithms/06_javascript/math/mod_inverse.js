function modInverse(a, m) {
  a = ((a % m) + m) % m;
  let old_r = a, r = m;
  let old_s = 1, s = 0;
  while (r !== 0) {
    const q = Math.floor(old_r / r);
    [old_r, r] = [r, old_r - q * r];
    [old_s, s] = [s, old_s - q * s];
  }
  return ((old_s % m) + m) % m;
}

module.exports = { modInverse };

if (require.main === module) {
  if (modInverse(3, 7) !== 5) throw new Error("mod inverse failed");
  if ((3 * modInverse(3, 1000000007)) % 1000000007 !== 1) throw new Error("mod inverse prime failed");
  console.log("[JavaScript Modular Inverse] Extended Euclid modular inverse verified");
}

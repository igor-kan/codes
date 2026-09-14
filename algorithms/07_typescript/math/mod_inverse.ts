export function modInverse(a: number, m: number): number {
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

if (modInverse(3, 7) !== 5) throw new Error("Modular inverse failed");
console.log("[TypeScript Modular Inverse] Extended Euclid modular inverse verified");

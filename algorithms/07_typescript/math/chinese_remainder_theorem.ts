/**
 * Chinese Remainder Theorem (CLRS 3rd Ed. Chapter 31.5)
 * Solves system of modular congruences: x = a_i (mod m_i) with pairwise coprime moduli.
 */

function extGCD(a: bigint, b: bigint): { gcd: bigint; x: bigint; y: bigint } {
  if (b === 0n) return { gcd: a, x: 1n, y: 0n };
  const { gcd, x: x1, y: y1 } = extGCD(b, a % b);
  return { gcd, x: y1, y: x1 - (a / b) * y1 };
}

function modInverse(a: bigint, m: bigint): bigint {
  const { gcd, x } = extGCD(a, m);
  if (gcd !== 1n) throw new Error("Inverse does not exist");
  return ((x % m) + m) % m;
}

export function chineseRemainderTheorem(remainders: bigint[], moduli: bigint[]): bigint {
  let prod = 1n;
  for (const m of moduli) prod *= m;

  let result = 0n;
  for (let i = 0; i < moduli.length; i++) {
    const pp = prod / moduli[i];
    const inv = modInverse(pp, moduli[i]);
    result = (result + remainders[i] * pp * inv) % prod;
  }
  return (result + prod) % prod;
}

const crtRem = [2n, 3n, 2n];
const crtMod = [3n, 5n, 7n];
const crtSol = chineseRemainderTheorem(crtRem, crtMod);
if (crtSol !== 23n) throw new Error("CRT failed");
console.log("CLRS Chinese Remainder Theorem verified successfully.");

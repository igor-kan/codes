/**
 * Extended Euclidean Algorithm (CLRS 3rd Ed. Chapter 31.2)
 * Computes gcd(a, b) and Bezout coefficients x and y such that a*x + b*y = gcd(a, b).
 */

export function extendedGCD(a: bigint, b: bigint): { gcd: bigint; x: bigint; y: bigint } {
  if (b === 0n) {
    return { gcd: a, x: 1n, y: 0n };
  }
  const { gcd, x: x1, y: y1 } = extendedGCD(b, a % b);
  const x = y1;
  const y = x1 - (a / b) * y1;
  return { gcd, x, y };
}

const egcdRes = extendedGCD(240n, 46n);
if (egcdRes.gcd !== 2n || 240n * egcdRes.x + 46n * egcdRes.y !== 2n) {
  throw new Error("Extended GCD failed");
}
console.log("CLRS Extended Euclidean Algorithm verified successfully.");

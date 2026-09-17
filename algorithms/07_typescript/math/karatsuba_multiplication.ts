/**
 * Karatsuba Fast Integer Multiplication (CLRS 3rd Ed. Chapter 4 Problems)
 * Divide-and-conquer large integer multiplication reducing 4 multiplications to 3.
 */

export function karatsuba(x: bigint, y: bigint): bigint {
  if (x < 10n || y < 10n) return x * y;

  const sx = x.toString();
  const sy = y.toString();
  const n = Math.max(sx.length, sy.length);
  const m = Math.floor(n / 2);

  const base = 10n ** BigInt(m);

  const xHigh = x / base;
  const xLow = x % base;
  const yHigh = y / base;
  const yLow = y % base;

  const z0 = karatsuba(xLow, yLow);
  const z2 = karatsuba(xHigh, yHigh);
  const z1 = karatsuba(xLow + xHigh, yLow + yHigh) - z2 - z0;

  return z2 * (10n ** BigInt(2 * m)) + z1 * base + z0;
}

const kA = 12345678901234567890n;
const kB = 98765432109876543210n;
if (karatsuba(kA, kB) !== kA * kB) throw new Error("Karatsuba multiplication failed");
console.log("Karatsuba Integer Multiplication verified successfully.");

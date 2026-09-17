/**
 * Halton Sequence (Numerical Recipes 3rd Ed. Chapter 7.7)
 * Multidimensional low-discrepancy quasi-random sequence for Quasi-Monte Carlo integration.
 */

function vanDerCorput(index: number, base: number): number {
  let f = 1;
  let r = 0;
  while (index > 0) {
    f /= base;
    r += f * (index % base);
    index = Math.floor(index / base);
  }
  return r;
}

export function haltonPoint(index: number, bases = [2, 3, 5]): number[] {
  return bases.map((b) => vanDerCorput(index, b));
}

const p1 = haltonPoint(1, [2, 3]);
const p2 = haltonPoint(2, [2, 3]);
if (p1[0] !== 0.5 || Math.abs(p1[1] - 1 / 3) > 1e-6) throw new Error("Halton sequence failed");
console.log("NR Halton Quasi-Random Sequence verified successfully.");

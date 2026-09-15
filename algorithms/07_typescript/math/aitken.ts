// Aitken's delta-squared acceleration.
function aitken(x0: number, x1: number, x2: number): number {
  const denominator = x2 - 2 * x1 + x0;
  if (Math.abs(denominator) < 1e-15) return x2;
  return x2 - (x2 - x1) ** 2 / denominator;
}

if (Math.abs(aitken(1, 0.5, 0.25)) > 1e-12) throw new Error("aitken geometric failed");
const sequence = [0, 1, 2].map((n) => 2 - 2 * 0.5 ** n);
if (Math.abs(aitken(sequence[0], sequence[1], sequence[2]) - 2) > 1e-12) throw new Error("aitken failed");
console.log("aitken verified");

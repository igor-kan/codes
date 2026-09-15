// Rayleigh quotient iteration.
function rayleighQuotient(matrix: number[][], vector: number[], iterations = 100): { eigenvalue: number; vector: number[] } {
  const n = matrix.length;
  let x = vector.map((value) => value / Math.max(...vector.map((v) => Math.abs(v))));
  let eigenvalue = 0;
  for (let iteration = 0; iteration < iterations; iteration += 1) {
    const product = matrix.map((row) => row.reduce((acc, value, j) => acc + value * x[j], 0));
    const norm = Math.max(...product.map((value) => Math.abs(value)));
    x = product.map((value) => value / norm);
    const numerator = x.reduce((acc, value, i) => acc + value * matrix[i].reduce((s, m, j) => s + m * x[j], 0), 0);
    const denominator = x.reduce((acc, value) => acc + value * value, 0);
    const next = numerator / denominator;
    if (Math.abs(next - eigenvalue) < 1e-12) return { eigenvalue: next, vector: x };
    eigenvalue = next;
  }
  return { eigenvalue, vector: x };
}

const { eigenvalue } = rayleighQuotient([[2, 1], [1, 2]], [1, 0]);
if (Math.abs(eigenvalue - 3) > 1e-9) throw new Error("rayleigh failed");
console.log(`eigenvalue=${eigenvalue}`);

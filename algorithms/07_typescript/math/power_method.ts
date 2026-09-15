// Power iteration for the dominant eigenvalue.
function powerMethod(matrix: number[][]): { eigenvalue: number; vector: number[] } {
  const n = matrix.length;
  let vector = new Array<number>(n).fill(1);
  let eigenvalue = 0;
  for (let iteration = 0; iteration < 1000; iteration += 1) {
    const product = matrix.map((row) => row.reduce((acc, value, j) => acc + value * vector[j], 0));
    const norm = Math.max(...product.map((value) => Math.abs(value)));
    vector = product.map((value) => value / norm);
    if (Math.abs(norm - eigenvalue) < 1e-12) { eigenvalue = norm; break; }
    eigenvalue = norm;
  }
  return { eigenvalue, vector };
}

const matrix = [[4, 1], [2, 3]];
const { eigenvalue, vector } = powerMethod(matrix);
if (Math.abs(eigenvalue - 5) > 1e-9) throw new Error("power method failed");
for (let i = 0; i < 2; i += 1) {
  const av = matrix[i].reduce((acc, value, j) => acc + value * vector[j], 0);
  if (Math.abs(av - eigenvalue * vector[i]) > 1e-9) throw new Error("power method eigenvector failed");
}
console.log(`dominant eigenvalue=${eigenvalue}`);

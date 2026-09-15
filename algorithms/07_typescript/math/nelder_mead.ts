// Nelder-Mead downhill simplex minimisation.
function nelderMead(f: (p: number[]) => number, start: number[], step = 0.5, tolerance = 1e-10, maxIterations = 2000): number[] {
  const n = start.length;
  const simplex: number[][] = [start.slice()];
  for (let i = 0; i < n; i += 1) {
    const point = start.slice();
    point[i] += step;
    simplex.push(point);
  }
  for (let iteration = 0; iteration < maxIterations; iteration += 1) {
    simplex.sort((a, b) => f(a) - f(b));
    const spread = Math.max(...Array.from({ length: n }, (_, i) => Math.abs(simplex[0][i] - simplex[n][i])));
    if (spread < tolerance) break;
    const centroid = Array.from({ length: n }, (_, i) =>
      simplex.slice(0, n).reduce((acc, point) => acc + point[i] / n, 0));
    const worst = simplex[n];
    const reflected = centroid.map((value, i) => value + (value - worst[i]));
    if (f(simplex[0]) <= f(reflected) && f(reflected) < f(simplex[n - 1])) {
      simplex[n] = reflected;
    } else if (f(reflected) < f(simplex[0])) {
      const expanded = centroid.map((value, i) => value + 2 * (value - worst[i]));
      simplex[n] = f(expanded) < f(reflected) ? expanded : reflected;
    } else {
      const contracted = centroid.map((value, i) => value + 0.5 * (worst[i] - value));
      if (f(contracted) < f(worst)) simplex[n] = contracted;
      else for (let j = 1; j <= n; j += 1) simplex[j] = simplex[j].map((value, i) => (simplex[0][i] + value) / 2);
    }
  }
  simplex.sort((a, b) => f(a) - f(b));
  return simplex[0];
}

const result = nelderMead((p) => (p[0] - 3) ** 2 + (p[1] + 2) ** 2, [0, 0]);
if (Math.abs(result[0] - 3) > 1e-4 || Math.abs(result[1] + 2) > 1e-4) throw new Error("nelder mead failed");
console.log(`minimum at ${result}`);

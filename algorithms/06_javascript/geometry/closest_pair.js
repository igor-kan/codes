// Closest pair of points (quadratic brute force).
const points = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]];
let best = Infinity;
for (let i = 0; i < points.length; i += 1) {
  for (let j = i + 1; j < points.length; j += 1) {
    best = Math.min(best, Math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1]));
  }
}
if (Math.abs(best - Math.SQRT2) > 1e-9) throw new Error("wrong closest distance");
console.log(`closest=${best}`);

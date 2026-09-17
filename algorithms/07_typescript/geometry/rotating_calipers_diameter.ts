/**
 * Rotating Calipers Algorithm (Michael Shamos)
 * Computes maximum distance (diameter) of a convex polygon in linear O(n) time.
 */

export interface PointR {
  x: number;
  y: number;
}

function distSq(p1: PointR, p2: PointR): number {
  return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2;
}

function cross(o: PointR, a: PointR, b: PointR): number {
  return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

export function polygonDiameter(hull: PointR[]): { maxDistance: number; pair: [PointR, PointR] } {
  const n = hull.length;
  if (n === 2) return { maxDistance: Math.sqrt(distSq(hull[0], hull[1])), pair: [hull[0], hull[1]] };

  let k = 1;
  while (cross(hull[n - 1], hull[0], hull[(k + 1) % n]) > cross(hull[n - 1], hull[0], hull[k])) {
    k = (k + 1) % n;
  }

  let maxD = 0;
  let bestPair: [PointR, PointR] = [hull[0], hull[0]];

  for (let i = 0, j = k; i <= k && j < n; i++) {
    while (cross(hull[i], hull[(i + 1) % n], hull[(j + 1) % n]) > cross(hull[i], hull[(i + 1) % n], hull[j])) {
      j = (j + 1) % n;
    }
    const d = distSq(hull[i], hull[j]);
    if (d > maxD) {
      maxD = d;
      bestPair = [hull[i], hull[j]];
    }
  }
  return { maxDistance: Math.sqrt(maxD), pair: bestPair };
}

const sqHull: PointR[] = [
  { x: 0, y: 0 },
  { x: 1, y: 0 },
  { x: 1, y: 1 },
  { x: 0, y: 1 },
];
const diamRes = polygonDiameter(sqHull);
if (Math.abs(diamRes.maxDistance - Math.SQRT2) > 1e-6) throw new Error("Rotating calipers failed");
console.log("Rotating Calipers verified successfully.");

/**
 * Graham Scan Convex Hull (CLRS 3rd Ed. Chapter 33.3)
 * Computes 2D convex hull of n points in O(n log n) utilizing cross product orientations.
 */

export interface Point {
  x: number;
  y: number;
}

function crossProduct(o: Point, a: Point, b: Point): number {
  return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

export function grahamScan(points: Point[]): Point[] {
  if (points.length <= 2) return [...points];

  // Find lowest point (break ties with lowest x)
  let p0 = points[0];
  for (const p of points) {
    if (p.y < p0.y || (p.y === p0.y && p.x < p0.x)) p0 = p;
  }

  // Sort by polar angle with p0
  const sorted = points.filter((p) => p !== p0).sort((a, b) => {
    const cp = crossProduct(p0, a, b);
    if (cp === 0) {
      const d1 = (a.x - p0.x) ** 2 + (a.y - p0.y) ** 2;
      const d2 = (b.x - p0.x) ** 2 + (b.y - p0.y) ** 2;
      return d1 - d2;
    }
    return -cp;
  });

  const hull: Point[] = [p0, sorted[0]];
  for (let i = 1; i < sorted.length; i++) {
    while (hull.length >= 2 && crossProduct(hull[hull.length - 2], hull[hull.length - 1], sorted[i]) <= 0) {
      hull.pop();
    }
    hull.push(sorted[i]);
  }
  return hull;
}

const pts: Point[] = [
  { x: 0, y: 3 },
  { x: 2, y: 2 },
  { x: 1, y: 1 },
  { x: 2, y: 1 },
  { x: 3, y: 0 },
  { x: 0, y: 0 },
  { x: 3, y: 3 },
];
const hull = grahamScan(pts);
if (hull.length !== 4) throw new Error("Graham Scan failed");
console.log("CLRS Graham Scan Convex Hull verified successfully.");

/**
 * Quickhull Algorithm
 * Divide-and-conquer convex hull algorithm analogous to Quicksort, running in average O(n log n).
 */

export interface PointQ {
  x: number;
  y: number;
}

function lineDistance(p1: PointQ, p2: PointQ, p: PointQ): number {
  return (p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x);
}

export function quickhull(points: PointQ[]): PointQ[] {
  if (points.length < 3) return [...points];

  let minX = points[0], maxX = points[0];
  for (const p of points) {
    if (p.x < minX.x) minX = p;
    if (p.x > maxX.x) maxX = p;
  }

  const hull: PointQ[] = [];
  hull.push(minX);
  hull.push(maxX);

  const leftSet: PointQ[] = [];
  const rightSet: PointQ[] = [];

  for (const p of points) {
    if (lineDistance(minX, maxX, p) > 0) leftSet.push(p);
    else if (lineDistance(maxX, minX, p) > 0) rightSet.push(p);
  }

  function findHull(p1: PointQ, p2: PointQ, set: PointQ[]): void {
    if (set.length === 0) return;

    let maxDist = -1;
    let furthest: PointQ = set[0];

    for (const p of set) {
      const d = lineDistance(p1, p2, p);
      if (d > maxDist) {
        maxDist = d;
        furthest = p;
      }
    }

    hull.push(furthest);

    const s1: PointQ[] = [];
    const s2: PointQ[] = [];
    for (const p of set) {
      if (lineDistance(p1, furthest, p) > 0) s1.push(p);
      if (lineDistance(furthest, p2, p) > 0) s2.push(p);
    }

    findHull(p1, furthest, s1);
    findHull(furthest, p2, s2);
  }

  findHull(minX, maxX, leftSet);
  findHull(maxX, minX, rightSet);

  return hull;
}

const ptsQ: PointQ[] = [
  { x: 0, y: 3 },
  { x: 2, y: 2 },
  { x: 1, y: 1 },
  { x: 2, y: 1 },
  { x: 3, y: 0 },
  { x: 0, y: 0 },
  { x: 3, y: 3 },
];
if (quickhull(ptsQ).length !== 4) throw new Error("Quickhull failed");
console.log("Quickhull verified successfully.");

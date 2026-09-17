/**
 * Jarvis March / Gift Wrapping (CLRS 3rd Ed. Chapter 33.3)
 * Output-sensitive 2D convex hull algorithm running in O(nh) time.
 */

export interface Point2 {
  x: number;
  y: number;
}

function orientation(p: Point2, q: Point2, r: Point2): number {
  const val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
  if (val === 0) return 0; // Collinear
  return val > 0 ? 1 : 2;  // 1: Clockwise, 2: Counterclockwise
}

export function jarvisMarch(points: Point2[]): Point2[] {
  const n = points.length;
  if (n < 3) return [...points];

  const hull: Point2[] = [];
  let l = 0;
  for (let i = 1; i < n; i++) {
    if (points[i].x < points[l].x) l = i;
  }

  let p = l;
  do {
    hull.push(points[p]);
    let q = (p + 1) % n;
    for (let i = 0; i < n; i++) {
      if (orientation(points[p], points[i], points[q]) === 2) {
        q = i;
      }
    }
    p = q;
  } while (p !== l);

  return hull;
}

const pts2: Point2[] = [
  { x: 0, y: 3 },
  { x: 2, y: 2 },
  { x: 1, y: 1 },
  { x: 2, y: 1 },
  { x: 3, y: 0 },
  { x: 0, y: 0 },
  { x: 3, y: 3 },
];
if (jarvisMarch(pts2).length !== 4) throw new Error("Jarvis March failed");
console.log("CLRS Jarvis March verified successfully.");

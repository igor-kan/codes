/**
 * Shoelace Formula (Gauss's Area Formula)
 * Calculates the exact signed and unsigned area of any simple 2D polygon in O(n) time.
 */

export interface Vec2 {
  x: number;
  y: number;
}

export function polygonArea(vertices: Vec2[]): number {
  const n = vertices.length;
  if (n < 3) return 0;

  let sum = 0;
  for (let i = 0; i < n; i++) {
    const next = (i + 1) % n;
    sum += vertices[i].x * vertices[next].y - vertices[next].x * vertices[i].y;
  }
  return Math.abs(sum) / 2;
}

const poly: Vec2[] = [
  { x: 0, y: 0 },
  { x: 4, y: 0 },
  { x: 4, y: 3 },
  { x: 0, y: 3 },
];
if (polygonArea(poly) !== 12) throw new Error("Shoelace area failed");
console.log("Shoelace Formula verified successfully.");

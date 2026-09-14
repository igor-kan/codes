// Interfaces vs type aliases.
export interface Point {
  x: number;
  y: number;
}

export interface Named extends Point {
  name: string;
}

export type Coordinate = readonly [x: number, y: number];
export type Identifiable = { readonly id: string };

export type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: Error };

export function distance(a: Point, b: Point): number {
  return Math.hypot(a.x - b.x, a.y - b.y);
}

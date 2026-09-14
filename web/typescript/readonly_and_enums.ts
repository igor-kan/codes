// Const assertions, enums and readonly arrays.
export const DIRECTIONS = ["north", "south", "east", "west"] as const;
export type Direction = (typeof DIRECTIONS)[number];

export enum Status {
  Idle = "idle",
  Loading = "loading",
  Done = "done",
}

export const HTTP_CODES = {
  ok: 200,
  notFound: 404,
  error: 500,
} as const;

export function isDirection(value: string): value is Direction {
  return (DIRECTIONS as readonly string[]).includes(value);
}

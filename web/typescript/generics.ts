// Generic functions and constraints.
export function first<T>(items: readonly T[]): T | undefined {
  return items[0];
}

export interface HasId {
  id: string;
}

export function indexById<T extends HasId>(items: T[]): Map<string, T> {
  return new Map(items.map((item) => [item.id, item]));
}

export function identity<const T>(value: T): T {
  return value;
}

const literal = identity({ kind: "circle", radius: 2 });

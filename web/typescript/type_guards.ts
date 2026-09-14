// User-defined type guards and assertions.
export type Fish = { swim: () => void };
export type Bird = { fly: () => void };

export function isFish(pet: Fish | Bird): pet is Fish {
  return "swim" in pet;
}

export function assertDefined<T>(value: T | null | undefined, label = "value"): asserts value is T {
  if (value === null || value === undefined) {
    throw new Error(`${label} is not defined`);
  }
}

export function move(pet: Fish | Bird): string {
  return isFish(pet) ? "swimming" : "flying";
}

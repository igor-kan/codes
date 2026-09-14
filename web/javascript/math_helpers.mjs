// Small numeric helpers used by the module examples.
export function add(values) {
  return values.reduce((sum, value) => sum + value, 0);
}

export function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

export const PI2 = Math.PI * 2;
export default { add, clamp, PI2 };

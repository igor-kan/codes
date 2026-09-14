// Closures and memoization.
export function makeCounter(start = 0) {
  let count = start;
  return {
    increment: () => ++count,
    value: () => count,
  };
}

export function memoize(fn) {
  const cache = new Map();
  return function memoized(...args) {
    const key = JSON.stringify(args);
    if (!cache.has(key)) cache.set(key, fn.apply(this, args));
    return cache.get(key);
  };
}

export const slowFib = memoize((n) => (n < 2 ? n : slowFib(n - 1) + slowFib(n - 2)));

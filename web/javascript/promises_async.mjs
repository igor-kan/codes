// Promises, async/await and concurrency control.
export function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function sequential(ids) {
  const results = [];
  for (const id of ids) {
    results.push(await delay(10) ?? id);
  }
  return results;
}

export async function parallel(ids) {
  return Promise.all(ids.map((id) => delay(10).then(() => id)));
}

export function settledSafely(promises) {
  return Promise.allSettled(promises);
}

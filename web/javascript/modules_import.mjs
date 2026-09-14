// ES module syntax: named, default, and namespace imports.
import { delay, parallel } from "./promises_async.mjs";
import * as math from "./math_helpers.mjs";

export const CONFIG = { retries: 3, timeout: 1000 };

export async function run(ids) {
  const values = await parallel(ids);
  return { sum: math.add(values), delayed: await delay(5) };
}

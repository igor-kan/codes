function quickselect(values, k) {
  const a = [...values];
  let lo = 0, hi = a.length - 1;
  while (true) {
    const pivot = a[hi];
    let i = lo;
    for (let j = lo; j < hi; j += 1) {
      if (a[j] < pivot) {
        [a[i], a[j]] = [a[j], a[i]];
        i += 1;
      }
    }
    [a[i], a[hi]] = [a[hi], a[i]];
    if (i === k) return a[i];
    if (k < i) hi = i - 1; else lo = i + 1;
  }
}

module.exports = { quickselect };

if (require.main === module) {
  const data = [3, 2, 1, 5, 6, 4];
  const sorted = [...data].sort((x, y) => x - y);
  for (let k = 0; k < data.length; k += 1) {
    if (quickselect(data, k) !== sorted[k]) throw new Error("quickselect failed");
  }
  console.log("[JavaScript Quickselect] order statistics verified");
}

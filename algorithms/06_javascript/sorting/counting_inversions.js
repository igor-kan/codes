function mergeCount(a, buf, lo, hi) {
  if (hi - lo <= 1) return 0;
  const mid = (lo + hi) >> 1;
  let inversions = mergeCount(a, buf, lo, mid) + mergeCount(a, buf, mid, hi);
  let i = lo, j = mid, k = lo;
  while (i < mid && j < hi) {
    if (a[i] <= a[j]) buf[k++] = a[i++];
    else { buf[k++] = a[j++]; inversions += mid - i; }
  }
  while (i < mid) buf[k++] = a[i++];
  while (j < hi) buf[k++] = a[j++];
  for (let t = lo; t < hi; t += 1) a[t] = buf[t];
  return inversions;
}

function countInversions(values) {
  const a = [...values];
  return mergeCount(a, new Array(a.length), 0, a.length);
}

module.exports = { countInversions };

if (require.main === module) {
  if (countInversions([2, 4, 1, 3, 5]) !== 3) throw new Error("inversion count failed");
  if (countInversions([5, 4, 3, 2, 1]) !== 10) throw new Error("reverse inversion count failed");
  console.log("[JavaScript Counting Inversions] merge-sort count verified");
}

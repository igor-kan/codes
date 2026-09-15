// Count inversions with a modified merge sort.
function mergeCount(a: number[], buf: number[], lo: number, hi: number): number {
  if (hi - lo <= 1) return 0;
  const mid = (lo + hi) >> 1;
  let inversions = mergeCount(a, buf, lo, mid) + mergeCount(a, buf, mid, hi);
  let i = lo;
  let j = mid;
  let k = lo;
  while (i < mid && j < hi) {
    if (a[i] <= a[j]) buf[k++] = a[i++];
    else { buf[k++] = a[j++]; inversions += mid - i; }
  }
  while (i < mid) buf[k++] = a[i++];
  while (j < hi) buf[k++] = a[j++];
  for (let t = lo; t < hi; t += 1) a[t] = buf[t];
  return inversions;
}

function countInversions(values: number[]): number {
  const a = [...values];
  return mergeCount(a, new Array<number>(a.length), 0, a.length);
}

if (countInversions([2, 4, 1, 3, 5]) !== 3) throw new Error("inversion count failed");
if (countInversions([5, 4, 3, 2, 1]) !== 10) throw new Error("reverse inversion count failed");
console.log("counting inversions verified");

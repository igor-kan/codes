function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  const m = arr.length >> 1;
  return merge(mergeSort(arr.slice(0,m)), mergeSort(arr.slice(m)));
}
function merge(l, r) {
  const res = []; let i=0, j=0;
  while (i<l.length && j<r.length) res.push(l[i]<=r[j] ? l[i++] : r[j++]);
  return [...res, ...l.slice(i), ...r.slice(j)];
}
module.exports = { mergeSort };
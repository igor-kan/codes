export function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  const m = arr.length >> 1;
  return merge(mergeSort(arr.slice(0,m)), mergeSort(arr.slice(m)));
}
function merge(l: number[], r: number[]): number[] {
  const res: number[] = []; let [i,j] = [0,0];
  while (i<l.length && j<r.length) res.push(l[i]<=r[j]?l[i++]:r[j++]);
  return [...res,...l.slice(i),...r.slice(j)];
}
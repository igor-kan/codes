function quickSort(arr) {
  if (arr.length <= 1) return arr;
  const pivot = arr[arr.length >> 1];
  const left = arr.filter(x => x < pivot);
  const mid  = arr.filter(x => x === pivot);
  const right= arr.filter(x => x > pivot);
  return [...quickSort(left), ...mid, ...quickSort(right)];
}
module.exports = { quickSort };
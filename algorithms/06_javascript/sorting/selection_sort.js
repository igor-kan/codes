function selectionSort(arr) {
  const a = arr.slice();
  for (let i = 0; i < a.length - 1; i++) {
    let minIdx = i;
    for (let j = i + 1; j < a.length; j++) if (a[j] < a[minIdx]) minIdx = j;
    if (minIdx !== i) [a[i], a[minIdx]] = [a[minIdx], a[i]];
  }
  return a;
}

module.exports = { selectionSort };

if (require.main === module) {
  const sorted = selectionSort([64, 25, 12, 22, 11]);
  if (sorted.join(",") !== "11,12,22,25,64") throw new Error("selection sort failed");
  console.log("[JavaScript Selection Sort] Sorted array verified");
}

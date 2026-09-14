function countingSort(arr) {
  if (arr.length === 0) return [];
  const max = Math.max(...arr);
  const count = new Array(max + 1).fill(0);
  for (const x of arr) count[x]++;
  const res = [];
  for (let i = 0; i <= max; i++) for (let j = 0; j < count[i]; j++) res.push(i);
  return res;
}

module.exports = { countingSort };

if (require.main === module) {
  const sorted = countingSort([4, 2, 2, 8, 3, 3, 1]);
  if (sorted.join(",") !== "1,2,2,3,3,4,8") throw new Error("counting sort failed");
  console.log("[JavaScript Counting Sort] Sorted array verified");
}

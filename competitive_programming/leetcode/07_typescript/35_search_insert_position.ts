function searchInsert(nums: number[], target: number): number {
  let low = 0;
  let high = nums.length;
  while (low < high) {
    const middle = (low + high) >> 1;
    if (nums[middle] < target) low = middle + 1;
    else high = middle;
  }
  return low;
}

if (searchInsert([1, 3, 5, 6], 5) !== 2 || searchInsert([1, 3, 5, 6], 2) !== 1) throw new Error("search insert failed");
if (searchInsert([1, 3, 5, 6], 7) !== 4 || searchInsert([1, 3, 5, 6], 0) !== 0) throw new Error("search insert failed");
console.log("35 search insert position ok");

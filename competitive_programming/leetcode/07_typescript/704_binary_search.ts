function binarySearch(nums: number[], target: number): number {
  let low = 0;
  let high = nums.length - 1;
  while (low <= high) {
    const middle = (low + high) >> 1;
    if (nums[middle] === target) return middle;
    if (nums[middle] < target) low = middle + 1;
    else high = middle - 1;
  }
  return -1;
}

if (binarySearch([-1, 0, 3, 5, 9, 12], 9) !== 4 || binarySearch([-1, 0, 3, 5, 9, 12], 2) !== -1) throw new Error("binary search failed");
console.log("704 binary search ok");

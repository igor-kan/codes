function containsDuplicate(nums) {
  return new Set(nums).size !== nums.length;
}

if (require.main === module) {
  if (containsDuplicate([1, 2, 3, 1]) !== true || containsDuplicate([1, 2, 3, 4]) !== false) throw new Error("contains duplicate failed");
  console.log("217 contains duplicate ok");
}

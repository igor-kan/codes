function missingNumber(nums) {
  const n = nums.length;
  return (n * (n + 1)) / 2 - nums.reduce((a, b) => a + b, 0);
}

if (require.main === module) {
  if (missingNumber([3, 0, 1]) !== 2 || missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) !== 8) throw new Error("missing number failed");
  console.log("268 missing number ok");
}

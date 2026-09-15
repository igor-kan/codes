function runningSum(nums) {
  const result = [];
  let total = 0;
  for (const value of nums) {
    total += value;
    result.push(total);
  }
  return result;
}

if (require.main === module) {
  if (runningSum([1, 2, 3, 4]).join(",") !== "1,3,6,10") throw new Error("running sum failed");
  if (runningSum([1, 1, 1, 1, 1]).join(",") !== "1,2,3,4,5") throw new Error("running sum failed");
  console.log("1480 running sum ok");
}

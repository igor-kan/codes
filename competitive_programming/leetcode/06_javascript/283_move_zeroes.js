function moveZeroes(nums) {
  const result = nums.filter((number) => number !== 0);
  while (result.length < nums.length) result.push(0);
  return result;
}

if (require.main === module) {
  if (moveZeroes([0, 1, 0, 3, 12]).join(",") !== "1,3,12,0,0") throw new Error("move zeroes failed");
  if (moveZeroes([0]).join(",") !== "0") throw new Error("move zeroes failed");
  console.log("283 move zeroes ok");
}

function removeElement(nums: number[], value: number): number[] {
  return nums.filter((number) => number !== value);
}

if (removeElement([3, 2, 2, 3], 3).join(",") !== "2,2") throw new Error("remove element failed");
if (removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2).join(",") !== "0,1,3,0,4") throw new Error("remove element failed");
console.log("27 remove element ok");

function removeDuplicates(nums: number[]): number[] {
  const result: number[] = [];
  for (const value of nums) if (result.length === 0 || result[result.length - 1] !== value) result.push(value);
  return result;
}

if (removeDuplicates([1, 1, 2]).join(",") !== "1,2") throw new Error("remove duplicates failed");
if (removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]).join(",") !== "0,1,2,3,4") throw new Error("remove duplicates failed");
console.log("26 remove duplicates ok");

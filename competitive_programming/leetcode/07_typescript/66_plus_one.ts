function plusOne(digits: number[]): number[] {
  const result = [...digits];
  for (let i = result.length - 1; i >= 0; i -= 1) {
    if (result[i] < 9) { result[i] += 1; return result; }
    result[i] = 0;
  }
  return [1, ...result];
}

if (plusOne([1, 2, 3]).join(",") !== "1,2,4") throw new Error("plus one failed");
if (plusOne([9, 9]).join(",") !== "1,0,0") throw new Error("plus one failed");
console.log("66 plus one ok");

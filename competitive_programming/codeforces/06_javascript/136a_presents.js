function presents(permutation) {
  const result = new Array(permutation.length).fill(0);
  permutation.forEach((giver, index) => { result[giver - 1] = index + 1; });
  return result;
}

if (require.main === module) {
  if (presents([2, 3, 4, 1]).join(",") !== "4,1,2,3") throw new Error("presents failed");
  console.log("136A presents ok");
}

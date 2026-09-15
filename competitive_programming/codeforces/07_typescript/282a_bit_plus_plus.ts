function bitPlusPlus(operations: string[]): number {
  let value = 0;
  for (const operation of operations) value += operation.includes("++") ? 1 : -1;
  return value;
}

if (bitPlusPlus(["++X", "X++", "--X"]) !== 1) throw new Error("bit++ failed");
if (bitPlusPlus(["X++", "X++", "X++", "X--"]) !== 2) throw new Error("bit++ failed");
console.log("282A bit++ ok");

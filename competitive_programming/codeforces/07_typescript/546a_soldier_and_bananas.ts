function soldierAndBananas(cost: number, money: number, count: number): number {
  const total = (cost * count * (count + 1)) / 2;
  return Math.max(0, total - money);
}

if (soldierAndBananas(3, 17, 4) !== 13) throw new Error("soldier and bananas failed");
if (soldierAndBananas(1, 100, 1) !== 0) throw new Error("soldier and bananas failed");
console.log("546A soldier and bananas ok");

function sqrtX(x: number): number {
  let low = 0;
  let high = x;
  while (low <= high) {
    const middle = Math.floor((low + high) / 2);
    if (middle * middle <= x) low = middle + 1;
    else high = middle - 1;
  }
  return high;
}

if (sqrtX(4) !== 2 || sqrtX(8) !== 2 || sqrtX(0) !== 0) throw new Error("sqrt x failed");
console.log("69 sqrt x ok");

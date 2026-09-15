function beautifulMatrix(grid) {
  for (let row = 0; row < 5; row += 1) {
    for (let column = 0; column < 5; column += 1) {
      if (grid[row][column] === 1) return Math.abs(row - 2) + Math.abs(column - 2);
    }
  }
  return -1;
}

if (require.main === module) {
  const grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
  ];
  if (beautifulMatrix(grid) !== 3) throw new Error("beautiful matrix failed");
  console.log("263A beautiful matrix ok");
}

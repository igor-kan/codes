function stonesOnTable(row: string): number {
  let removals = 0;
  for (let i = 1; i < row.length; i += 1) if (row[i] === row[i - 1]) removals += 1;
  return removals;
}

if (stonesOnTable("RRG") !== 1 || stonesOnTable("RRRRR") !== 4 || stonesOnTable("BRBG") !== 0) {
  throw new Error("stones on the table failed");
}
console.log("266A stones on the table ok");

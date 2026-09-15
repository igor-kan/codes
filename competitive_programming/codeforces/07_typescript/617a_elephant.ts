function elephant(position: number): number {
  return Math.floor((position + 4) / 5);
}

if (elephant(5) !== 1 || elephant(12) !== 3 || elephant(1) !== 1) throw new Error("elephant failed");
console.log("617A elephant ok");

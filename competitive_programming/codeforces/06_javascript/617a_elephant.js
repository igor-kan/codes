function elephant(position) {
  return Math.floor((position + 4) / 5);
}

if (require.main === module) {
  if (elephant(5) !== 1 || elephant(12) !== 3 || elephant(1) !== 1) throw new Error("elephant failed");
  console.log("617A elephant ok");
}

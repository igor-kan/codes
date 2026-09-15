function watermelon(weight) {
  return weight % 2 === 0 && weight > 2 ? "YES" : "NO";
}

if (require.main === module) {
  if (watermelon(8) !== "YES" || watermelon(2) !== "NO" || watermelon(3) !== "NO") throw new Error("watermelon failed");
  console.log("4A watermelon ok");
}

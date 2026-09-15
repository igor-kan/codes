function nearlyLuckyNumber(number) {
  const count = String(number).split("").filter((digit) => digit === "4" || digit === "7").length;
  return count === 4 || count === 7 ? "YES" : "NO";
}

if (require.main === module) {
  if (nearlyLuckyNumber(47) !== "NO") throw new Error("nearly lucky failed");
  if (nearlyLuckyNumber(7747774) !== "YES") throw new Error("nearly lucky failed");
  if (nearlyLuckyNumber(40047) !== "NO") throw new Error("nearly lucky failed");
  console.log("110A nearly lucky number ok");
}

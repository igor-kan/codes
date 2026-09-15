function reverseInteger(x) {
  const sign = x < 0 ? -1 : 1;
  const reversed = sign * Number(String(Math.abs(x)).split("").reverse().join(""));
  return reversed >= -(2 ** 31) && reversed <= 2 ** 31 - 1 ? reversed : 0;
}

if (require.main === module) {
  if (reverseInteger(123) !== 321 || reverseInteger(-123) !== -321 || reverseInteger(120) !== 21) throw new Error("reverse integer failed");
  if (reverseInteger(1534236469) !== 0) throw new Error("reverse integer overflow failed");
  console.log("7 reverse integer ok");
}

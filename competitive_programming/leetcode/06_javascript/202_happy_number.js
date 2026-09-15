function happyNumber(n) {
  const seen = new Set();
  let value = n;
  while (value !== 1 && !seen.has(value)) {
    seen.add(value);
    value = String(value).split("").reduce((acc, digit) => acc + Number(digit) ** 2, 0);
  }
  return value === 1;
}

if (require.main === module) {
  if (happyNumber(19) !== true || happyNumber(2) !== false) throw new Error("happy number failed");
  console.log("202 happy number ok");
}

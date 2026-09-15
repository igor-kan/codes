function numberOf1Bits(n) {
  let value = n >>> 0;
  let count = 0;
  while (value) {
    count += value & 1;
    value >>>= 1;
  }
  return count;
}

if (require.main === module) {
  if (numberOf1Bits(11) !== 3 || numberOf1Bits(128) !== 1 || numberOf1Bits(4294967293) !== 31) throw new Error("number of 1 bits failed");
  console.log("191 number of 1 bits ok");
}

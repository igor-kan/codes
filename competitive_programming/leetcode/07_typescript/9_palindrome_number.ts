function palindromeNumber(x: number): boolean {
  return x >= 0 && String(x) === String(x).split("").reverse().join("");
}

if (palindromeNumber(121) !== true || palindromeNumber(-121) !== false || palindromeNumber(10) !== false) throw new Error("palindrome number failed");
console.log("9 palindrome number ok");

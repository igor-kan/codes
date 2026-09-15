function validAnagram(s, t) {
  return s.split("").sort().join("") === t.split("").sort().join("");
}

if (require.main === module) {
  if (validAnagram("anagram", "nagaram") !== true || validAnagram("rat", "car") !== false) throw new Error("valid anagram failed");
  console.log("242 valid anagram ok");
}

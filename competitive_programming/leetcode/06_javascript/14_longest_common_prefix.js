function longestCommonPrefix(strs) {
  if (strs.length === 0) return "";
  let prefix = strs[0];
  for (const word of strs.slice(1)) {
    while (!word.startsWith(prefix)) {
      prefix = prefix.slice(0, -1);
      if (!prefix) return "";
    }
  }
  return prefix;
}

if (require.main === module) {
  if (longestCommonPrefix(["flower", "flow", "flight"]) !== "fl") throw new Error("longest common prefix failed");
  if (longestCommonPrefix(["dog", "racecar", "car"]) !== "") throw new Error("longest common prefix failed");
  console.log("14 longest common prefix ok");
}

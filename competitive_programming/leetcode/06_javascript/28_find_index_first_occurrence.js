function strStr(haystack, needle) {
  return haystack.indexOf(needle);
}

if (require.main === module) {
  if (strStr("sadbutsad", "sad") !== 0 || strStr("leetcode", "leeto") !== -1) throw new Error("strStr failed");
  console.log("28 find index first occurrence ok");
}

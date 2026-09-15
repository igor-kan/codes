function strStr(haystack: string, needle: string): number {
  return haystack.indexOf(needle);
}

if (strStr("sadbutsad", "sad") !== 0 || strStr("leetcode", "leeto") !== -1) throw new Error("strStr failed");
console.log("28 find index first occurrence ok");

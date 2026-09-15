function lengthOfLastWord(text) {
  const words = text.trim().split(/\s+/).filter(Boolean);
  return words.length ? words[words.length - 1].length : 0;
}

if (require.main === module) {
  if (lengthOfLastWord("Hello World") !== 5) throw new Error("length of last word failed");
  if (lengthOfLastWord("   fly me   to   the moon  ") !== 4) throw new Error("length of last word failed");
  console.log("58 length of last word ok");
}

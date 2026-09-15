function stringTask(text) {
  const vowels = "aeiouy";
  let result = "";
  for (const character of text.toLowerCase()) {
    if (!vowels.includes(character)) result += `.${character}`;
  }
  return result;
}

if (require.main === module) {
  if (stringTask("Codeforces") !== ".c.d.f.r.c.s") throw new Error("string task failed");
  if (stringTask("aBAcAba") !== ".b.c.b") throw new Error("string task failed");
  console.log("118A string task ok");
}

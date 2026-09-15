function petyaAndStrings(a: string, b: string): number {
  const left = a.toLowerCase();
  const right = b.toLowerCase();
  if (left < right) return -1;
  if (left > right) return 1;
  return 0;
}

if (petyaAndStrings("aaaa", "aaaA") !== 0) throw new Error("petya failed");
if (petyaAndStrings("abs", "Abz") !== -1) throw new Error("petya failed");
if (petyaAndStrings("abcdefg", "AbCdEfF") !== 1) throw new Error("petya failed");
console.log("112A petya and strings ok");

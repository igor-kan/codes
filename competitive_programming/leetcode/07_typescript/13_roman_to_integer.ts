const VALUES: Record<string, number> = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };

function romanToInteger(text: string): number {
  let total = 0;
  for (let i = 0; i < text.length; i += 1) {
    const value = VALUES[text[i]];
    if (i + 1 < text.length && value < VALUES[text[i + 1]]) total -= value;
    else total += value;
  }
  return total;
}

if (romanToInteger("III") !== 3 || romanToInteger("LVIII") !== 58 || romanToInteger("MCMXCIV") !== 1994) throw new Error("roman to integer failed");
console.log("13 roman to integer ok");

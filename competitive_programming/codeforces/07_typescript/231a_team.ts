function team(problems: number[][]): number {
  return problems.filter(([a, b, c]) => a + b + c >= 2).length;
}

if (team([[1, 1, 0], [1, 1, 1], [1, 0, 0]]) !== 2) throw new Error("team failed");
console.log("231A team ok");

function helpfulMaths(expression: string): string {
  return expression.split("+").sort().join("+");
}

if (helpfulMaths("3+2+1") !== "1+2+3") throw new Error("helpful maths failed");
if (helpfulMaths("1+1+3+1+3") !== "1+1+1+3+3") throw new Error("helpful maths failed");
console.log("339A helpful maths ok");

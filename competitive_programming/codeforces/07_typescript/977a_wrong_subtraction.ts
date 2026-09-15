function wrongSubtraction(number: number, steps: number): number {
  let current = number;
  for (let i = 0; i < steps; i += 1) {
    if (current % 10 === 0) current /= 10;
    else current -= 1;
  }
  return current;
}

if (wrongSubtraction(512, 4) !== 50) throw new Error("wrong subtraction failed");
if (wrongSubtraction(1000000000, 9) !== 1) throw new Error("wrong subtraction failed");
console.log("977A wrong subtraction ok");

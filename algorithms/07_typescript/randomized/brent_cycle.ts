// Brent's cycle detection algorithm.
function brentCycle(nextNode: (value: number) => number, start: number): { mu: number; lambda: number } {
  let power = 1;
  let lam = 1;
  let tortoise = start;
  let hare = nextNode(start);
  while (tortoise !== hare) {
    if (power === lam) { tortoise = hare; power *= 2; lam = 0; }
    hare = nextNode(hare);
    lam += 1;
  }
  tortoise = start;
  hare = start;
  for (let i = 0; i < lam; i += 1) hare = nextNode(hare);
  let mu = 0;
  while (tortoise !== hare) { tortoise = nextNode(tortoise); hare = nextNode(hare); mu += 1; }
  return { mu, lambda: lam };
}

const link = [1, 2, 3, 4, 3];
const { mu, lambda } = brentCycle((i) => link[i], 0);
if (mu !== 3 || lambda !== 2) throw new Error("brent cycle failed");
console.log(`mu=${mu}, lambda=${lambda}`);

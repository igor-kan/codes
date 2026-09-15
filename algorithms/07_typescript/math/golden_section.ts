// Golden-section search for a 1D minimum.
function goldenSection(f: (x: number) => number, a0: number, b0: number): number {
  const invPhi = (Math.sqrt(5) - 1) / 2;
  let a = a0;
  let b = b0;
  let c = b - invPhi * (b - a);
  let d = a + invPhi * (b - a);
  let fc = f(c);
  let fd = f(d);
  while (b - a > 1e-9) {
    if (fc < fd) {
      b = d; d = c; fd = fc;
      c = b - invPhi * (b - a); fc = f(c);
    } else {
      a = c; c = d; fc = fd;
      d = a + invPhi * (b - a); fd = f(d);
    }
  }
  return (a + b) / 2;
}

const x = goldenSection((v) => (v - 3) * (v - 3), -10, 10);
if (Math.abs(x - 3) > 1e-6) throw new Error("golden section failed");
console.log(`argmin=${x}`);

function verlet(acceleration, x0, v0, dt, steps) {
  let x = x0;
  let v = v0;
  for (let i = 0; i < steps; i += 1) {
    const a = acceleration(x);
    const xNew = x + v * dt + 0.5 * a * dt * dt;
    const aNew = acceleration(xNew);
    v = v + 0.5 * (a + aNew) * dt;
    x = xNew;
  }
  return { position: x, velocity: v };
}

module.exports = { verlet };

if (require.main === module) {
  const { position, velocity } = verlet((x) => -x, 1, 0, 0.001, 10000);
  const energy = 0.5 * (velocity * velocity + position * position);
  if (Math.abs(energy - 0.5) > 1e-3) throw new Error("verlet energy failed");
  if (Math.abs(position - Math.cos(10)) > 1e-2) throw new Error("verlet position failed");
  console.log("[JavaScript Verlet] harmonic oscillator verified");
}

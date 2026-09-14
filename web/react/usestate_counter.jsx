// State with the useState hook and derived values.
import { useState } from "react";

export function Counter({ initial = 0, step = 1 }) {
  const [count, setCount] = useState(initial);
  const parity = count % 2 === 0 ? "even" : "odd";

  return (
    <div>
      <output>{count} ({parity})</output>
      <button type="button" onClick={() => setCount((c) => c + step)}>+</button>
      <button type="button" onClick={() => setCount((c) => c - step)}>-</button>
      <button type="button" onClick={() => setCount(initial)}>reset</button>
    </div>
  );
}

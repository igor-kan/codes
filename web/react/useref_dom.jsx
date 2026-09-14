// Refs for DOM access and mutable instance values.
import { useEffect, useRef, useState } from "react";

export function AutoFocusInput() {
  const inputRef = useRef(null);
  const renders = useRef(0);
  const [value, setValue] = useState("");

  useEffect(() => {
    renders.current += 1;
    inputRef.current?.focus();
  });

  return (
    <div>
      <input ref={inputRef} value={value} onChange={(e) => setValue(e.target.value)} />
      <p>Value: {value} (renders: {renders.current})</p>
    </div>
  );
}

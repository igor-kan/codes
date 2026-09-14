// Performance hooks: memo, useMemo and useCallback.
import { memo, useCallback, useMemo, useState } from "react";

const Row = memo(function Row({ item, onPick }) {
  return <li onClick={() => onPick(item.id)}>{item.label}</li>;
});

export function FilteredList({ items, query }) {
  const [selected, setSelected] = useState(null);

  const filtered = useMemo(
    () => items.filter((item) => item.label.toLowerCase().includes(query.toLowerCase())),
    [items, query],
  );

  const handlePick = useCallback((id) => setSelected(id), []);

  return (
    <div>
      <ul>{filtered.map((item) => <Row key={item.id} item={item} onPick={handlePick} />)}</ul>
      <p>Selected: {selected ?? "none"}</p>
    </div>
  );
}

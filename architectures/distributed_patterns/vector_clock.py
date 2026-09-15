"""Vector clocks for tracking causality."""
class VectorClock:
    def __init__(self, values: dict[str, int] | None = None) -> None:
        self.values: dict[str, int] = dict(values or {})

    def increment(self, node: str) -> "VectorClock":
        self.values[node] = self.values.get(node, 0) + 1
        return self

    def merge(self, other: "VectorClock") -> "VectorClock":
        return VectorClock({k: max(self.values.get(k, 0), other.values.get(k, 0))
                            for k in set(self.values) | set(other.values)})

    def relation(self, other: "VectorClock") -> str:
        keys = set(self.values) | set(other.values)
        less = all(self.values.get(k, 0) <= other.values.get(k, 0) for k in keys)
        greater = all(self.values.get(k, 0) >= other.values.get(k, 0) for k in keys)
        if less and not greater:
            return "before"
        if greater and not less:
            return "after"
        if less and greater:
            return "equal"
        return "concurrent"


if __name__ == "__main__":
    a = VectorClock().increment("a")
    b = VectorClock().increment("b")
    assert a.relation(a.merge(b)) == "before"
    assert b.relation(a) == "concurrent"
    print("vector clock ok")

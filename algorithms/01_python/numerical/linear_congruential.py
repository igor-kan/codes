"""Linear congruential generator (Numerical Recipes 7.1)."""
class LinearCongruential:
    def __init__(self, seed: int = 1, a: int = 1664525, c: int = 1013904223,
                 modulus: int = 2 ** 32) -> None:
        self.state = seed
        self.a, self.c, self.modulus = a, c, modulus

    def next_int(self) -> int:
        self.state = (self.a * self.state + self.c) % self.modulus
        return self.state

    def next_float(self) -> float:
        return self.next_int() / self.modulus


if __name__ == "__main__":
    rng = LinearCongruential(seed=42)
    values = [rng.next_float() for _ in range(1000)]
    assert all(0.0 <= v < 1.0 for v in values)
    assert 0.4 < sum(values) / len(values) < 0.6
    print("linear congruential generator ok")

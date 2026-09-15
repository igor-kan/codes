"""Reservoir sampling for a uniform sample of a stream (CLRS 5.3)."""
import random


def reservoir_sample(stream, k: int, seed: int = 0) -> list:
    rng = random.Random(seed)
    reservoir: list = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = rng.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir


if __name__ == "__main__":
    data = list(range(100))
    sample = reservoir_sample(data, 5, seed=42)
    assert len(sample) == 5 and len(set(sample)) == 5
    assert all(0 <= value < 100 for value in sample)
    print("reservoir sampling ok")

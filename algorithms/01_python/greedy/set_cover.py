"""Greedy set cover approximation (CLRS 35.3)."""
def set_cover(universe, subsets):
    uncovered = set(universe)
    chosen = []
    while uncovered:
        best = max(subsets, key=lambda subset: len(uncovered & subset))
        if not (uncovered & best):
            break
        chosen.append(best)
        uncovered -= best
    return chosen


if __name__ == "__main__":
    universe = {1, 2, 3, 4, 5}
    subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
    chosen = set_cover(universe, subsets)
    assert len(chosen) == 2
    covered = set()
    for subset in chosen:
        covered |= subset
    assert covered == universe
    print("set cover ok")

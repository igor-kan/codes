"""Stationary distribution of a Markov chain via iteration."""
def step(transition: list[list[float]], state: list[float]) -> list[float]:
    n = len(state)
    return [sum(state[i] * transition[i][j] for i in range(n)) for j in range(n)]


def stationary(transition: list[list[float]], iterations: int = 1000) -> list[float]:
    n = len(transition)
    state = [1 / n] * n
    for _ in range(iterations):
        state = step(transition, state)
    return state


if __name__ == "__main__":
    # Weather: sunny<->rainy with equal persistence.
    transition = [[0.9, 0.1], [0.5, 0.5]]
    pi = stationary(transition)
    assert abs(sum(pi) - 1) < 1e-9
    assert abs(pi[0] - 5 / 6) < 1e-3
    print(f"stationary: {[round(p, 4) for p in pi]}")

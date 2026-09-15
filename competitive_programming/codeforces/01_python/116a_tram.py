"""Codeforces 116A - Tram."""
def tram(stops):
    current = 0
    capacity = 0
    for leaving, entering in stops:
        current -= leaving
        current += entering
        capacity = max(capacity, current)
    return capacity


if __name__ == "__main__":
    assert tram([(0, 3), (2, 5), (4, 2), (4, 0)]) == 6
    print("116A tram ok")

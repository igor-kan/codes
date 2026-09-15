"""Brent's cycle detection algorithm (Brent 1980)."""
def brent_cycle(next_node, start):
    power = lam = 1
    tortoise = start
    hare = next_node(start)
    while tortoise != hare:
        if power == lam:
            tortoise = hare
            power *= 2
            lam = 0
        hare = next_node(hare)
        lam += 1
    tortoise = hare = start
    for _ in range(lam):
        hare = next_node(hare)
    mu = 0
    while tortoise != hare:
        tortoise = next_node(tortoise)
        hare = next_node(hare)
        mu += 1
    return mu, lam


if __name__ == "__main__":
    link = [1, 2, 3, 4, 3]
    assert brent_cycle(lambda i: link[i], 0) == (3, 2)
    print("brent cycle ok")

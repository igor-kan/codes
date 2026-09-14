def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[rv] = ru
    return True


if __name__ == "__main__":
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    assert not valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    print("ok")

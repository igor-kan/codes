"""Transitive closure of a directed graph (CLRS 25.2)."""
def transitive_closure(adjacency: list[list[bool]]) -> list[list[bool]]:
    n = len(adjacency)
    reach = [row[:] for row in adjacency]
    for i in range(n):
        reach[i][i] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
    return reach


if __name__ == "__main__":
    # 0 -> 1 -> 2
    graph = [[False, True, False], [False, False, True], [False, False, False]]
    reach = transitive_closure(graph)
    assert reach[0][2] and not reach[2][0]
    print("transitive closure ok")

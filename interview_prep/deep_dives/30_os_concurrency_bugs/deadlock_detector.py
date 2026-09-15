"""Deadlock detection via cycle search in a wait-for graph."""


def find_cycle(graph: dict[int, int]) -> list[int] | None:
    visited: set[int] = set()
    stack: set[int] = set()
    path: list[int] = []

    def dfs(node: int) -> list[int] | None:
        visited.add(node)
        stack.add(node)
        path.append(node)
        neighbor = graph.get(node)
        if neighbor is not None:
            if neighbor in stack:
                return path[path.index(neighbor):] + [neighbor]
            if neighbor not in visited:
                result = dfs(neighbor)
                if result:
                    return result
        path.pop()
        stack.discard(node)
        return None

    for node in graph:
        if node not in visited:
            cycle = dfs(node)
            if cycle:
                return cycle
    return None


if __name__ == "__main__":
    deadlocked = {1: 2, 2: 3, 3: 1}
    assert find_cycle(deadlocked) == [1, 2, 3, 1]
    assert find_cycle({1: 2, 2: 3, 3: 4}) is None
    print("deadlock detector ok")

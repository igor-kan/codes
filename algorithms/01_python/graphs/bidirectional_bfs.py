"""Bidirectional BFS shortest path on an unweighted graph."""
from collections import deque


def bidirectional_bfs(graph: dict[int, list[int]], source: int, target: int) -> int:
    if source == target:
        return 0
    front, back = {source}, {target}
    visited = {source, target}
    distance = 0
    while front and back:
        distance += 1
        if len(front) > len(back):
            front, back = back, front
        next_front = set()
        for node in front:
            for neighbor in graph.get(node, []):
                if neighbor in back:
                    return distance
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_front.add(neighbor)
        front = next_front
    return -1


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1, 5], 4: [2, 5], 5: [3, 4]}
    assert bidirectional_bfs(graph, 0, 5) == 3
    print("bidirectional bfs ok")

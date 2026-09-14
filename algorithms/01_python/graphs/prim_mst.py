"""Minimum spanning tree with Prim's algorithm."""
import heapq


def prim_mst(graph: dict[str, list[tuple[str, int]]]) -> int:
    if not graph:
        return 0
    start = next(iter(graph))
    visited = {start}
    heap = [(weight, start, node) for node, weight in graph[start]]
    heapq.heapify(heap)
    total = 0
    while heap and len(visited) < len(graph):
        weight, _, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        total += weight
        for neighbor, w in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (w, node, neighbor))
    return total


if __name__ == "__main__":
    graph = {
        "A": [("B", 2), ("D", 6)],
        "B": [("A", 2), ("C", 3), ("D", 8), ("E", 5)],
        "C": [("B", 3), ("E", 7)],
        "D": [("A", 6), ("B", 8), ("E", 9)],
        "E": [("B", 5), ("C", 7), ("D", 9)],
    }
    print(prim_mst(graph))  # 16

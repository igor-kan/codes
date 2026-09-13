"""A* Shortest Path Search Algorithm on 2D Grid.

Heuristic search algorithm utilizing priority queues to compute optimal paths
with admissible Euclidean and Manhattan heuristics.
"""

import heapq
from typing import List, Tuple, Optional, Set, Dict

Coord = Tuple[int, int]

def manhattan_heuristic(a: Coord, b: Coord) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_grid(grid: List[List[int]], start: Coord, goal: Coord) -> Optional[List[Coord]]:
    """Computes shortest path from start to goal in 0/1 grid (0=passable, 1=obstacle)."""
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] != 0 or grid[goal[0]][goal[1]] != 0:
        return None

    # Priority queue storing (f_score, cost_so_far, current_coord)
    pq: List[Tuple[int, int, Coord]] = []
    heapq.heappush(pq, (manhattan_heuristic(start, goal), 0, start))

    came_from: Dict[Coord, Optional[Coord]] = {start: None}
    cost_so_far: Dict[Coord, int] = {start: 0}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        _, current_cost, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct path
            path: List[Coord] = []
            curr: Optional[Coord] = current
            while curr is not None:
                path.append(curr)
                curr = came_from[curr]
            path.reverse()
            return path

        if current_cost > cost_so_far[current]:
            continue

        for dr, dc in moves:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_cost = current_cost + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + manhattan_heuristic(neighbor, goal)
                    heapq.heappush(pq, (priority, new_cost, neighbor))
                    came_from[neighbor] = current

    return None

if __name__ == "__main__":
    test_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    path = a_star_grid(test_grid, (0, 0), (4, 4))
    assert path is not None, "A* pathfinding failed to find optimal route"
    assert len(path) == 17, f"Expected length 13, got {len(path)}"
    print(f"[Python A*] Path computed successfully: {len(path)} steps.")

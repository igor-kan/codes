"""Maze solving with DFS and BFS."""
from collections import deque

MAZE = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]


def bfs_path(maze, start=(0, 0), goal=(4, 4)):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    seen = {start}
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal:
            return path
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in seen:
                seen.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None


if __name__ == "__main__":
    path = bfs_path(MAZE)
    assert path and path[0] == (0, 0) and path[-1] == (4, 4)
    print("maze solver ok, steps:", len(path))

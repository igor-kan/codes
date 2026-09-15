"""Rat in a maze: find all paths to the exit."""
def find_paths(maze: list[list[int]]) -> list[str]:
    n = len(maze)
    results: list[str] = []
    visited = [[False] * n for _ in range(n)]

    def backtrack(r: int, c: int, path: str) -> None:
        if r == n - 1 and c == n - 1:
            results.append(path)
            return
        for dr, dc, move in ((1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                backtrack(nr, nc, path + move)
                visited[nr][nc] = False

    if maze[0][0] == 1:
        visited[0][0] = True
        backtrack(0, 0, "")
    return sorted(results)


if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    paths = find_paths(maze)
    assert "DRDDRR" in paths
    print("rat in maze ok")

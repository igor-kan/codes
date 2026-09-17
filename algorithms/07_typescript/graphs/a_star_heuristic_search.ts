/**
 * A* Pathfinding Algorithm
 * Heuristic graph search finding shortest path with admissible evaluation f(n) = g(n) + h(n).
 */

export interface Point2D {
  x: number;
  y: number;
}

export function aStarSearch(
  grid: number[][],
  start: Point2D,
  goal: Point2D
): Point2D[] | null {
  const rows = grid.length;
  const cols = grid[0].length;
  const key = (p: Point2D) => `${p.x},${p.y}`;

  const heuristic = (a: Point2D, b: Point2D) => Math.abs(a.x - b.x) + Math.abs(a.y - b.y);

  const openSet = new Map<string, Point2D>();
  openSet.set(key(start), start);

  const cameFrom = new Map<string, Point2D>();
  const gScore = new Map<string, number>();
  gScore.set(key(start), 0);

  const fScore = new Map<string, number>();
  fScore.set(key(start), heuristic(start, goal));

  while (openSet.size > 0) {
    let currentKey = "";
    let minF = Infinity;
    for (const [k, p] of openSet.entries()) {
      const f = fScore.get(k) ?? Infinity;
      if (f < minF) {
        minF = f;
        currentKey = k;
      }
    }

    const current = openSet.get(currentKey)!;
    if (current.x === goal.x && current.y === goal.y) {
      const path: Point2D[] = [current];
      let curr = current;
      while (cameFrom.has(key(curr))) {
        curr = cameFrom.get(key(curr))!;
        path.push(curr);
      }
      return path.reverse();
    }

    openSet.delete(currentKey);

    const neighbors: Point2D[] = [
      { x: current.x + 1, y: current.y },
      { x: current.x - 1, y: current.y },
      { x: current.x, y: current.y + 1 },
      { x: current.x, y: current.y - 1 },
    ];

    for (const nb of neighbors) {
      if (nb.x < 0 || nb.x >= cols || nb.y < 0 || nb.y >= rows || grid[nb.y][nb.x] === 1) continue;
      const tentativeG = (gScore.get(key(current)) ?? Infinity) + 1;
      if (tentativeG < (gScore.get(key(nb)) ?? Infinity)) {
        cameFrom.set(key(nb), current);
        gScore.set(key(nb), tentativeG);
        fScore.set(key(nb), tentativeG + heuristic(nb, goal));
        openSet.set(key(nb), nb);
      }
    }
  }
  return null;
}

const grid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0],
];
const path = aStarSearch(grid, { x: 0, y: 0 }, { x: 2, y: 2 });
if (!path || path.length !== 5) throw new Error("A* search failed");
console.log("A* Search verified successfully.");

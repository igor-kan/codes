import java.util.*;

public class AStar {

    public static class Point {
        public final int r, c;
        public Point(int r, int c) { this.r = r; this.c = c; }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Point)) return false;
            Point p = (Point) o;
            return r == p.r && c == p.c;
        }

        @Override
        public int hashCode() {
            return Objects.hash(r, c);
        }
    }

    private static class Node implements Comparable<Node> {
        final Point pt;
        final int fScore;
        final int gScore;

        Node(Point pt, int fScore, int gScore) {
            this.pt = pt;
            this.fScore = fScore;
            this.gScore = gScore;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.fScore, o.fScore);
        }
    }

    private static int manhattan(Point a, Point b) {
        return Math.abs(a.r - b.r) + Math.abs(a.c - b.c);
    }

    public static List<Point> findPath(int[][] grid, Point start, Point goal) {
        int rows = grid.length;
        int cols = grid[0].length;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        Map<Point, Integer> gScore = new HashMap<>();
        Map<Point, Point> cameFrom = new HashMap<>();

        gScore.put(start, 0);
        pq.add(new Node(start, manhattan(start, goal), 0));

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (curr.pt.equals(goal)) {
                List<Point> path = new ArrayList<>();
                Point step = goal;
                while (step != null) {
                    path.add(step);
                    step = cameFrom.get(step);
                }
                Collections.reverse(path);
                return path;
            }

            if (curr.gScore > gScore.getOrDefault(curr.pt, Integer.MAX_VALUE)) {
                continue;
            }

            for (int[] d : dirs) {
                int nr = curr.pt.r + d[0];
                int nc = curr.pt.c + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 0) {
                    Point neighbor = new Point(nr, nc);
                    int tentativeG = curr.gScore + 1;
                    if (tentativeG < gScore.getOrDefault(neighbor, Integer.MAX_VALUE)) {
                        gScore.put(neighbor, tentativeG);
                        cameFrom.put(neighbor, curr.pt);
                        pq.add(new Node(neighbor, tentativeG + manhattan(neighbor, goal), tentativeG));
                    }
                }
            }
        }
        return Collections.emptyList();
    }

    public static void main(String[] args) {
        int[][] grid = {
            {0, 0, 0, 0, 0},
            {1, 1, 1, 1, 0},
            {0, 0, 0, 0, 0},
            {0, 1, 1, 1, 1},
            {0, 0, 0, 0, 0}
        };
        List<Point> path = findPath(grid, new Point(0, 0), new Point(4, 4));
        if (path.size() != 17) {
            throw new AssertionError("Expected 17 steps, got " + path.size());
        }
        System.out.println("[Java A*] Path computed successfully: " + path.size() + " steps.");
    }
}

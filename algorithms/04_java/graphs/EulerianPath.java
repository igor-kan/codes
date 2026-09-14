import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EulerianPath {
    // Hierholzer's algorithm for a directed graph; returns an Eulerian path/circuit, or null if none.
    public static List<Integer> eulerianPath(int n, int[][] edges) {
        List<Deque<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayDeque<>());
        int[] indeg = new int[n], outdeg = new int[n];
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            outdeg[e[0]]++;
            indeg[e[1]]++;
        }
        int start = -1, end = -1;
        for (int i = 0; i < n; i++) {
            if (outdeg[i] - indeg[i] == 1) {
                if (start != -1) return null;
                start = i;
            } else if (indeg[i] - outdeg[i] == 1) {
                if (end != -1) return null;
                end = i;
            } else if (indeg[i] != outdeg[i]) {
                return null;
            }
        }
        if (start == -1) {
            for (int i = 0; i < n; i++) if (outdeg[i] > 0) { start = i; break; }
        }
        if (start == -1) start = 0;

        Deque<Integer> stack = new ArrayDeque<>();
        List<Integer> path = new ArrayList<>();
        stack.push(start);
        while (!stack.isEmpty()) {
            int u = stack.peek();
            Deque<Integer> neighbors = adj.get(u);
            if (neighbors.isEmpty()) {
                path.add(u);
                stack.pop();
            } else {
                stack.push(neighbors.pollFirst());
            }
        }
        Collections.reverse(path);
        if (path.size() != edges.length + 1) return null;
        return path;
    }

    public static void main(String[] args) {
        int[][] edges = {{0, 1}, {1, 2}, {2, 0}};
        List<Integer> path = eulerianPath(3, edges);
        if (path == null || path.size() != 4) throw new AssertionError("Eulerian circuit should have 4 vertices");
        if (!path.get(0).equals(path.get(path.size() - 1))) throw new AssertionError("circuit should start and end at same vertex");
        Map<String, Integer> used = new HashMap<>();
        for (int i = 0; i < path.size() - 1; i++) {
            String key = path.get(i) + "->" + path.get(i + 1);
            used.put(key, used.getOrDefault(key, 0) + 1);
        }
        for (int[] e : edges) {
            String key = e[0] + "->" + e[1];
            if (used.getOrDefault(key, 0) == 0) throw new AssertionError("missing edge " + key);
        }
        System.out.println("[Java EulerianPath] Hierholzer's algorithm verified: " + path);
    }
}

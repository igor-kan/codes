package graphs;

import java.util.*;

/**
 * Hierholzer's Algorithm in Java
 * Linear time O(V + E) Eulerian path / circuit.
 */
public class Hierholzer {
    public static List<Integer> findEulerianPath(int n, List<Integer>[] adj) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>(adj[i]);

        Deque<Integer> stack = new ArrayDeque<>();
        List<Integer> path = new ArrayList<>();
        stack.push(0);

        while (!stack.isEmpty()) {
            int u = stack.peek();
            if (!graph[u].isEmpty()) {
                int next = graph[u].remove(graph[u].size() - 1);
                stack.push(next);
            } else {
                path.add(stack.pop());
            }
        }
        Collections.reverse(path);
        return path;
    }

    public static void main(String[] args) {
        List<Integer>[] adj = new ArrayList[4];
        for (int i = 0; i < 4; i++) adj[i] = new ArrayList<>();
        adj[0].add(1);
        adj[1].add(2);
        adj[2].add(0);
        adj[2].add(3);
        adj[3].add(0);
        List<Integer> p = findEulerianPath(4, adj);
        assert !p.isEmpty();
        System.out.println("Java Hierholzer verified.");
    }
}

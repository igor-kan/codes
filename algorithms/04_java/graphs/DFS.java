import java.util.*;

public class DFS {
    public static List<Integer> traverse(Map<Integer, List<Integer>> graph, int start) {
        Set<Integer> visited = new HashSet<>();
        Deque<Integer> stack = new ArrayDeque<>();
        List<Integer> order = new ArrayList<>();
        stack.push(start);
        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (visited.add(node)) {
                order.add(node);
                List<Integer> neighbors = graph.getOrDefault(node, Collections.emptyList());
                for (int i = neighbors.size() - 1; i >= 0; i--) stack.push(neighbors.get(i));
            }
        }
        return order;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(0, 3, 4));
        graph.put(2, Arrays.asList(0, 5));
        graph.put(3, Collections.singletonList(1));
        graph.put(4, Collections.singletonList(1));
        graph.put(5, Collections.singletonList(2));

        List<Integer> order = traverse(graph, 0);
        if (order.size() != 6 || order.get(0) != 0) throw new AssertionError("unexpected traversal");
        System.out.println("[Java DFS] Iterative stack-based traversal verified: " + order);
    }
}

package algorithms.graphs;

import java.util.*;

public class AStar {
    static class Node implements Comparable<Node> {
        int id;
        double f, g, h;
        public Node(int id, double g, double h) { this.id = id; this.g = g; this.h = h; this.f = g + h; }
        public int compareTo(Node o) { return Double.compare(this.f, o.f); }
    }

    public static List<Integer> findPath(Map<Integer, List<int[]>> graph, int start, int goal, Map<Integer, Double> heuristics) {
        PriorityQueue<Node> openSet = new PriorityQueue<>();
        Map<Integer, Integer> cameFrom = new HashMap<>();
        Map<Integer, Double> gScore = new HashMap<>();
        
        openSet.add(new Node(start, 0, heuristics.getOrDefault(start, 0.0)));
        gScore.put(start, 0.0);

        while (!openSet.isEmpty()) {
            Node current = openSet.poll();
            if (current.id == goal) {
                List<Integer> path = new ArrayList<>();
                int curr = current.id;
                while (cameFrom.containsKey(curr)) {
                    path.add(curr);
                    curr = cameFrom.get(curr);
                }
                path.add(start);
                Collections.reverse(path);
                return path;
            }

            for (int[] neighbor : graph.getOrDefault(current.id, Collections.emptyList())) {
                int next = neighbor[0];
                double weight = neighbor[1];
                double tentativeGScore = gScore.getOrDefault(current.id, Double.MAX_VALUE) + weight;

                if (tentativeGScore < gScore.getOrDefault(next, Double.MAX_VALUE)) {
                    cameFrom.put(next, current.id);
                    gScore.put(next, tentativeGScore);
                    openSet.add(new Node(next, tentativeGScore, heuristics.getOrDefault(next, 0.0)));
                }
            }
        }
        return Collections.emptyList();
    }
}

import java.util.*;

public class DijkstraFull {
    static class Edge {
        int to;
        int weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    static class Node implements Comparable<Node> {
        int id;
        int dist;

        Node(int id, int dist) {
            this.id = id;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.dist, o.dist);
        }
    }

    public static int[] dijkstra(int n, List<List<Edge>> adj, int source) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[source] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(source, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (curr.dist > dist[curr.id]) continue;

            for (Edge edge : adj.get(curr.id)) {
                if (dist[curr.id] + edge.weight < dist[edge.to]) {
                    dist[edge.to] = dist[curr.id] + edge.weight;
                    pq.add(new Node(edge.to, dist[edge.to]));
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        int n = 4;
        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        adj.get(0).add(new Edge(1, 4));
        adj.get(0).add(new Edge(2, 1));
        adj.get(2).add(new Edge(1, 2));
        adj.get(1).add(new Edge(3, 1));
        adj.get(2).add(new Edge(3, 5));

        int[] dist = dijkstra(n, adj, 0);
        assert dist[3] == 4;
        System.out.println("[Java Dijkstra] Shortest path 0 -> 3: " + dist[3] + " verified.");
    }
}

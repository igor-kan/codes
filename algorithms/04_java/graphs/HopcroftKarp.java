package graphs;

import java.util.*;

/**
 * Hopcroft-Karp Algorithm in Java
 * Maximum cardinality bipartite matching in O(E sqrt(V)).
 */
public class HopcroftKarp {
    private final int nU, nV;
    private final List<Integer>[] adj;
    private final int[] pairU, pairV, dist;

    @SuppressWarnings("unchecked")
    public HopcroftKarp(int u, int v) {
        this.nU = u;
        this.nV = v;
        this.adj = new ArrayList[u + 1];
        for (int i = 0; i <= u; i++) adj[i] = new ArrayList<>();
        this.pairU = new int[u + 1];
        this.pairV = new int[v + 1];
        this.dist = new int[u + 1];
    }

    public void addEdge(int u, int v) {
        adj[u].add(v);
    }

    public int maxMatching() {
        int matching = 0;
        while (bfs()) {
            for (int u = 1; u <= nU; u++) {
                if (pairU[u] == 0 && dfs(u)) matching++;
            }
        }
        return matching;
    }

    private boolean bfs() {
        Queue<Integer> q = new LinkedList<>();
        for (int u = 1; u <= nU; u++) {
            if (pairU[u] == 0) {
                dist[u] = 0;
                q.add(u);
            } else dist[u] = Integer.MAX_VALUE;
        }
        dist[0] = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] < dist[0]) {
                for (int v : adj[u]) {
                    if (dist[pairV[v]] == Integer.MAX_VALUE) {
                        dist[pairV[v]] = dist[u] + 1;
                        q.add(pairV[v]);
                    }
                }
            }
        }
        return dist[0] != Integer.MAX_VALUE;
    }

    private boolean dfs(int u) {
        if (u != 0) {
            for (int v : adj[u]) {
                if (dist[pairV[v]] == dist[u] + 1 && dfs(pairV[v])) {
                    pairV[v] = u;
                    pairU[u] = v;
                    return true;
                }
            }
            dist[u] = Integer.MAX_VALUE;
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        HopcroftKarp hk = new HopcroftKarp(4, 4);
        hk.addEdge(1, 2);
        hk.addEdge(1, 3);
        hk.addEdge(2, 1);
        hk.addEdge(3, 2);
        hk.addEdge(4, 2);
        hk.addEdge(4, 4);
        assert hk.maxMatching() == 4;
        System.out.println("Java Hopcroft-Karp verified.");
    }
}

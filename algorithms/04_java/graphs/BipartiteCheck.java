import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

public class BipartiteCheck {
    public static boolean isBipartite(int n, List<List<Integer>> adj) {
        int[] color = new int[n];
        Arrays.fill(color, -1);
        for (int s = 0; s < n; s++) {
            if (color[s] != -1) continue;
            Deque<Integer> q = new ArrayDeque<>();
            color[s] = 0;
            q.add(s);
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : adj.get(u)) {
                    if (color[v] == -1) {
                        color[v] = color[u] ^ 1;
                        q.add(v);
                    } else if (color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int n = 4;
        List<List<Integer>> bip = new ArrayList<>();
        for (int i = 0; i < n; i++) bip.add(new ArrayList<>());
        bip.get(0).add(1); bip.get(0).add(3);
        bip.get(1).add(0); bip.get(1).add(2);
        bip.get(2).add(1); bip.get(2).add(3);
        bip.get(3).add(0); bip.get(3).add(2);
        if (!isBipartite(n, bip)) throw new AssertionError("graph should be bipartite");

        List<List<Integer>> notBip = new ArrayList<>();
        for (int i = 0; i < 3; i++) notBip.add(new ArrayList<>());
        notBip.get(0).add(1); notBip.get(1).add(0);
        notBip.get(1).add(2); notBip.get(2).add(1);
        notBip.get(2).add(0); notBip.get(0).add(2);
        if (isBipartite(3, notBip)) throw new AssertionError("triangle should not be bipartite");
        System.out.println("[Java BipartiteCheck] Bipartite check verified");
    }
}

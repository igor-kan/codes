import java.util.ArrayDeque;
import java.util.Deque;

// Gale-Shapley stable matching.
public class StableMarriage {
    public static void main(String[] args) {
        int[][] menPref = {{0, 1, 2}, {1, 0, 2}, {0, 1, 2}};
        int[][] womenPref = {{2, 1, 0}, {0, 1, 2}, {0, 1, 2}};
        int n = 3;
        int[][] rank = new int[n][n];
        for (int w = 0; w < n; w++) {
            for (int i = 0; i < n; i++) rank[w][womenPref[w][i]] = i;
        }
        Deque<Integer> free = new ArrayDeque<>();
        for (int m = 0; m < n; m++) free.push(m);
        int[] next = new int[n];
        int[] engagedTo = {-1, -1, -1};
        while (!free.isEmpty()) {
            int m = free.pop();
            int w = menPref[m][next[m]++];
            if (engagedTo[w] == -1) {
                engagedTo[w] = m;
            } else if (rank[w][m] < rank[w][engagedTo[w]]) {
                free.push(engagedTo[w]);
                engagedTo[w] = m;
            } else {
                free.push(m);
            }
        }
        assert engagedTo[0] == 2 && engagedTo[1] == 0 && engagedTo[2] == 1;
        System.out.println("stable marriage ok");
    }
}

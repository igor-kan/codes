import java.util.*;

// Codeforces 158A - Next Round.
public class NextRound {
    static int nextRound(int[] scores, int k) {
        int threshold = scores[k - 1];
        int count = 0;
        for (int score : scores) if (score >= threshold && score > 0) count++;
        return count;
    }

    public static void main(String[] args) {
        assert nextRound(new int[] {10, 9, 8, 7, 7, 7, 5, 5}, 5) == 6;
        assert nextRound(new int[] {0, 0, 0, 0}, 2) == 0;
        System.out.println("158A next round ok");
    }
}

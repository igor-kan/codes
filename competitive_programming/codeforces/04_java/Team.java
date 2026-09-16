import java.util.*;

// Codeforces 231A - Team.
public class Team {
    static int team(int[][] problems) {
        int count = 0;
        for (int[] p : problems) if (p[0] + p[1] + p[2] >= 2) count++;
        return count;
    }

    public static void main(String[] args) {
        assert team(new int[][] {{1, 1, 0}, {1, 1, 1}, {1, 0, 0}}) == 2;
        System.out.println("231A team ok");
    }
}

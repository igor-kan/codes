import java.util.*;

// Codeforces 116A - Tram.
public class Tram {
    static int tram(int[][] stops) {
        int current = 0, capacity = 0;
        for (int[] stop : stops) {
            current = current - stop[0] + stop[1];
            capacity = Math.max(capacity, current);
        }
        return capacity;
    }

    public static void main(String[] args) {
        assert tram(new int[][] {{0, 3}, {2, 5}, {4, 2}, {4, 0}}) == 6;
        System.out.println("116A tram ok");
    }
}

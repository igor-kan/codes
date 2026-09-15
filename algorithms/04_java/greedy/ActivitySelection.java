import java.util.Arrays;
import java.util.Comparator;

// Activity-selection problem (CLRS 16.1).
public class ActivitySelection {
    static class Activity {
        int start, finish;
        Activity(int s, int f) { start = s; finish = f; }
    }

    public static void main(String[] args) {
        Activity[] acts = {
            new Activity(1, 4), new Activity(3, 5), new Activity(0, 6),
            new Activity(5, 7), new Activity(3, 9), new Activity(5, 9),
            new Activity(6, 10), new Activity(8, 11), new Activity(8, 12),
            new Activity(2, 14), new Activity(12, 16)
        };
        Arrays.sort(acts, Comparator.comparingInt(a -> a.finish));
        int count = 0, last = -1;
        for (Activity a : acts) {
            if (a.start >= last) { count++; last = a.finish; }
        }
        assert count == 4;
        System.out.println("activity selection ok");
    }
}

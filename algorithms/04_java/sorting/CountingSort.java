import java.util.Arrays;

public class CountingSort {
    // Sorts non-negative integers in [0, maxVal].
    public static int[] sort(int[] a, int maxVal) {
        int[] count = new int[maxVal + 1];
        for (int x : a) count[x]++;
        for (int i = 1; i <= maxVal; i++) count[i] += count[i - 1];
        int[] out = new int[a.length];
        for (int i = a.length - 1; i >= 0; i--) out[--count[a[i]]] = a[i];
        return out;
    }

    public static void main(String[] args) {
        int[] data = {3, 1, 3, 0, 2, 1, 5, 4, 2};
        int[] sorted = sort(data, 5);
        for (int i = 1; i < sorted.length; i++)
            if (sorted[i - 1] > sorted[i]) throw new AssertionError("not sorted at " + i);
        System.out.println("[Java CountingSort] Counting sort verified: " + Arrays.toString(sorted));
    }
}

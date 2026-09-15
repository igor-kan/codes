import java.util.Arrays;

// Quickselect: expected linear-time order statistic (CLRS 9.2).
public class Quickselect {
    static int quickselect(int[] a, int k) {
        int lo = 0, hi = a.length - 1;
        while (true) {
            int pivot = a[hi], i = lo;
            for (int j = lo; j < hi; j++) {
                if (a[j] < pivot) {
                    int t = a[i]; a[i++] = a[j]; a[j] = t;
                }
            }
            int t = a[i]; a[i] = a[hi]; a[hi] = t;
            if (i == k) return a[i];
            if (k < i) hi = i - 1; else lo = i + 1;
        }
    }

    public static void main(String[] args) {
        int[] data = {3, 2, 1, 5, 6, 4};
        int[] sorted = data.clone();
        Arrays.sort(sorted);
        for (int k = 0; k < data.length; k++) {
            assert quickselect(data.clone(), k) == sorted[k];
        }
        System.out.println("quickselect ok");
    }
}

import java.util.function.IntPredicate;

public class BinarySearch {
    public static int lowerBound(int[] a, int key) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] < key) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    public static int upperBound(int[] a, int key) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] <= key) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    // Largest x in [lo,hi] with pred(x) true (pred monotone false -> true).
    public static int lastTrue(int lo, int hi, IntPredicate pred) {
        while (lo < hi) {
            int mid = (lo + hi + 1) >>> 1;
            if (pred.test(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 2, 2, 3, 4, 5};
        if (lowerBound(a, 2) != 1) throw new AssertionError("lowerBound(2) should be 1");
        if (upperBound(a, 2) != 4) throw new AssertionError("upperBound(2) should be 4");
        if (lowerBound(a, 6) != 7) throw new AssertionError("lowerBound(6) should be 7");
        int ans = lastTrue(1, 100, x -> (long) x * x <= 30);
        if (ans != 5) throw new AssertionError("largest x with x^2<=30 should be 5");
        System.out.println("[Java BinarySearch] lowerBound/upperBound + search on answer verified");
    }
}

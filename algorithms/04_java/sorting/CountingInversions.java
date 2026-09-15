// Count inversions with a modified merge sort (CLRS 2.4 style).
public class CountingInversions {
    static long mergeCount(int[] a, int[] buf, int lo, int hi) {
        if (hi - lo <= 1) return 0;
        int mid = (lo + hi) / 2;
        long inversions = mergeCount(a, buf, lo, mid) + mergeCount(a, buf, mid, hi);
        int i = lo, j = mid, k = lo;
        while (i < mid && j < hi) {
            if (a[i] <= a[j]) buf[k++] = a[i++];
            else { buf[k++] = a[j++]; inversions += mid - i; }
        }
        while (i < mid) buf[k++] = a[i++];
        while (j < hi) buf[k++] = a[j++];
        System.arraycopy(buf, lo, a, lo, hi - lo);
        return inversions;
    }

    static long countInversions(int[] a) {
        return mergeCount(a, new int[a.length], 0, a.length);
    }

    public static void main(String[] args) {
        assert countInversions(new int[]{2, 4, 1, 3, 5}) == 3;
        assert countInversions(new int[]{5, 4, 3, 2, 1}) == 10;
        System.out.println("counting inversions ok");
    }
}

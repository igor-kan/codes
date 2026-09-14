public class TernarySearch {
    // Finds the index of the minimum of a unimodal array (strictly decreasing then increasing).
    public static int ternarySearchMin(double[] f) {
        int lo = 0, hi = f.length - 1;
        while (hi - lo > 2) {
            int m1 = lo + (hi - lo) / 3;
            int m2 = hi - (hi - lo) / 3;
            if (f[m1] < f[m2]) hi = m2;
            else lo = m1;
        }
        int best = lo;
        for (int i = lo; i <= hi; i++) if (f[i] < f[best]) best = i;
        return best;
    }

    public static void main(String[] args) {
        double[] f = {10, 8, 5, 3, 4, 6, 9, 12};
        int idx = ternarySearchMin(f);
        if (idx != 3 || f[idx] != 3) throw new AssertionError("min index should be 3, got " + idx);
        System.out.println("[Java TernarySearch] Unimodal minimum at index " + idx + " verified");
    }
}

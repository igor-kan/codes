public class SlidingWindow {
    public static int maxSumFixed(int[] a, int k) {
        int sum = 0;
        for (int i = 0; i < k; i++) sum += a[i];
        int best = sum;
        for (int i = k; i < a.length; i++) {
            sum += a[i] - a[i - k];
            best = Math.max(best, sum);
        }
        return best;
    }

    public static void main(String[] args) {
        int[] a = {2, 1, 5, 1, 3, 2};
        int k = 3;
        if (maxSumFixed(a, k) != 9) throw new AssertionError("max window sum should be 9");
        System.out.println("[Java SlidingWindow] Fixed-size window max sum verified: " + maxSumFixed(a, k));
    }
}

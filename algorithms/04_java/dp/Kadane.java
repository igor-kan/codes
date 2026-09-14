public class Kadane {
    public static int maxSubarraySum(int[] a) {
        int best = Integer.MIN_VALUE, cur = 0;
        for (int x : a) {
            cur = Math.max(x, cur + x);
            best = Math.max(best, cur);
        }
        return best;
    }

    public static void main(String[] args) {
        int[] a = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        if (maxSubarraySum(a) != 6) throw new AssertionError("max subarray sum should be 6");
        int[] neg = {-5, -2, -3};
        if (maxSubarraySum(neg) != -2) throw new AssertionError("max subarray sum should be -2");
        System.out.println("[Java Kadane] Max subarray sum verified: " + maxSubarraySum(a));
    }
}

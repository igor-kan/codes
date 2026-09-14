public class TwoPointers {
    public static int[] twoSumSorted(int[] a, int target) {
        int lo = 0, hi = a.length - 1;
        while (lo < hi) {
            int sum = a[lo] + a[hi];
            if (sum == target) return new int[]{lo, hi};
            else if (sum < target) lo++;
            else hi--;
        }
        return null;
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 6};
        int[] res = twoSumSorted(a, 6);
        if (res == null || res[0] != 1 || res[1] != 3) throw new AssertionError("two-sum failed");
        if (twoSumSorted(a, 20) != null) throw new AssertionError("expected no pair");
        System.out.println("[Java TwoPointers] Two-sum on sorted array verified: indices " + res[0] + "," + res[1]);
    }
}

import java.util.ArrayList;
import java.util.List;

public class LIS {
    public static int lengthOfLIS(int[] nums) {
        List<Integer> tails = new ArrayList<>();
        for (int x : nums) {
            int lo = 0, hi = tails.size();
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (tails.get(mid) < x) lo = mid + 1;
                else hi = mid;
            }
            if (lo == tails.size()) tails.add(x);
            else tails.set(lo, x);
        }
        return tails.size();
    }

    public static void main(String[] args) {
        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};
        if (lengthOfLIS(nums) != 4) throw new AssertionError("LIS should be 4");
        int[] inc = {1, 2, 3, 4, 5};
        if (lengthOfLIS(inc) != 5) throw new AssertionError("LIS should be 5");
        System.out.println("[Java LIS] Longest increasing subsequence O(n log n) verified: " + lengthOfLIS(nums));
    }
}

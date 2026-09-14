import java.util.ArrayList;
import java.util.List;

public class Backtracking {
    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrackSubsets(nums, 0, new ArrayList<>(), res);
        return res;
    }

    private static void backtrackSubsets(int[] nums, int start, List<Integer> cur, List<List<Integer>> res) {
        res.add(new ArrayList<>(cur));
        for (int i = start; i < nums.length; i++) {
            cur.add(nums[i]);
            backtrackSubsets(nums, i + 1, cur, res);
            cur.remove(cur.size() - 1);
        }
    }

    public static List<List<Integer>> permutations(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrackPermutations(nums, new boolean[nums.length], new ArrayList<>(), res);
        return res;
    }

    private static void backtrackPermutations(int[] nums, boolean[] used, List<Integer> cur, List<List<Integer>> res) {
        if (cur.size() == nums.length) {
            res.add(new ArrayList<>(cur));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            cur.add(nums[i]);
            backtrackPermutations(nums, used, cur, res);
            cur.remove(cur.size() - 1);
            used[i] = false;
        }
    }

    public static List<List<Integer>> combinations(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrackCombinations(n, k, 1, new ArrayList<>(), res);
        return res;
    }

    private static void backtrackCombinations(int n, int k, int start, List<Integer> cur, List<List<Integer>> res) {
        if (cur.size() == k) {
            res.add(new ArrayList<>(cur));
            return;
        }
        for (int i = start; i <= n; i++) {
            cur.add(i);
            backtrackCombinations(n, k, i + 1, cur, res);
            cur.remove(cur.size() - 1);
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        if (subsets(nums).size() != 8) throw new AssertionError("subsets of 3 elements should be 8");
        if (permutations(nums).size() != 6) throw new AssertionError("permutations of 3 elements should be 6");
        if (combinations(5, 2).size() != 10) throw new AssertionError("C(5,2) should be 10");
        System.out.println("[Java Backtracking] Subsets, permutations, combinations verified");
    }
}

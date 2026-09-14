import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class MonotonicStack {
    public static int[] nextGreaterElement(int[] a) {
        int n = a.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && a[stack.peek()] < a[i]) {
                res[stack.pop()] = a[i];
            }
            stack.push(i);
        }
        return res;
    }

    public static void main(String[] args) {
        int[] a = {4, 5, 2, 10, 8};
        int[] nge = nextGreaterElement(a);
        int[] expected = {5, 10, 10, -1, -1};
        if (!Arrays.equals(nge, expected)) throw new AssertionError("NGE mismatch: " + Arrays.toString(nge));
        System.out.println("[Java MonotonicStack] Next greater element verified: " + Arrays.toString(nge));
    }
}

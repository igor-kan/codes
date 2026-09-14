import java.util.Arrays;

public class ZAlgorithm {
    public static int[] zFunction(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) z[i]++;
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }

    public static void main(String[] args) {
        String s = "aabcaabxaaaz";
        int[] z = zFunction(s);
        int[] expected = {0, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0};
        for (int i = 0; i < s.length(); i++)
            if (z[i] != expected[i]) throw new AssertionError("Z mismatch at " + i + ": " + z[i]);
        System.out.println("[Java ZAlgorithm] Z-function verified: " + Arrays.toString(z));
    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class KMP {

    public static int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;

        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    public static List<Integer> search(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        List<Integer> occurrences = new ArrayList<>();
        if (m == 0 || n == 0) return occurrences;

        int[] lps = computeLPS(pattern);
        int i = 0, j = 0;

        while (i < n) {
            if (text.charAt(i) == pattern.charAt(j)) {
                i++;
                j++;
            }

            if (j == m) {
                occurrences.add(i - j);
                j = lps[j - 1];
            } else if (i < n && text.charAt(i) != pattern.charAt(j)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }

        return occurrences;
    }

    public static void main(String[] args) {
        String txt = "ABABDABACDABABCABABABABCABAB";
        String pat = "ABABCABAB";
        List<Integer> matches = search(txt, pat);

        if (!matches.equals(Arrays.asList(10, 19))) {
            throw new AssertionError("KMP failed to locate correct pattern indices.");
        }

        System.out.println("[Java KMP] Pattern matches verified at: " + matches);
    }
}

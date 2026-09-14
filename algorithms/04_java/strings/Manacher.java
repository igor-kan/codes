public class Manacher {
    public static int longestPalindromicSubstring(String s) {
        if (s == null || s.isEmpty()) return 0;
        StringBuilder sb = new StringBuilder("#");
        for (int i = 0; i < s.length(); i++) sb.append(s.charAt(i)).append('#');
        String t = sb.toString();
        int n = t.length();
        int[] p = new int[n];
        int c = 0, r = 0, maxLen = 0;
        for (int i = 0; i < n; i++) {
            int mirror = 2 * c - i;
            if (i < r) p[i] = Math.min(r - i, p[mirror]);
            int a = i + (1 + p[i]);
            int b = i - (1 + p[i]);
            while (a < n && b >= 0 && t.charAt(a) == t.charAt(b)) {
                p[i]++;
                a++;
                b--;
            }
            if (i + p[i] > r) {
                c = i;
                r = i + p[i];
            }
            maxLen = Math.max(maxLen, p[i]);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        if (longestPalindromicSubstring("babad") != 3) throw new AssertionError("LPS of babad should be 3");
        if (longestPalindromicSubstring("cbbd") != 2) throw new AssertionError("LPS of cbbd should be 2");
        if (longestPalindromicSubstring("racecar") != 7) throw new AssertionError("LPS of racecar should be 7");
        System.out.println("[Java Manacher] Longest palindromic substring verified");
    }
}

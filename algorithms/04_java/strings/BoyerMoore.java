public final class BoyerMoore {
    private BoyerMoore() {}

    public static int search(String text, String pattern) {
        int n = text.length(), m = pattern.length();
        int[] skip = new int[256];
        for (int i = 0; i < 256; i++) {
            skip[i] = m;
        }
        for (int i = 0; i < m - 1; i++) {
            skip[pattern.charAt(i)] = m - 1 - i;
        }
        int i = 0;
        while (i <= n - m) {
            int j = m - 1;
            while (j >= 0 && text.charAt(i + j) == pattern.charAt(j)) {
                j--;
            }
            if (j < 0) {
                return i;
            }
            i += skip[text.charAt(i + m - 1)];
        }
        return -1;
    }

    public static void main(String[] args) {
        if (search("here is a simple example", "example") != 17 || search("abc", "xyz") != -1) {
            throw new AssertionError("search failed");
        }
        System.out.println("boyer-moore ok");
    }
}

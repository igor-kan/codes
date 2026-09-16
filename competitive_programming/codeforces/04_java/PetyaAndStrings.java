import java.util.*;

// Codeforces 112A - Petya and Strings.
public class PetyaAndStrings {
    static int petyaAndStrings(String a, String b) {
        int comparison = a.toLowerCase().compareTo(b.toLowerCase());
        return Integer.compare(comparison, 0);
    }

    public static void main(String[] args) {
        assert petyaAndStrings("aaaa", "aaaA") == 0;
        assert petyaAndStrings("abs", "Abz") == -1;
        assert petyaAndStrings("abcdefg", "AbCdEfF") == 1;
        System.out.println("112A petya and strings ok");
    }
}

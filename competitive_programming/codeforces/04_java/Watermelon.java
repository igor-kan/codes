import java.util.*;

// Codeforces 4A - Watermelon.
public class Watermelon {
    static String watermelon(int weight) {
        return weight % 2 == 0 && weight > 2 ? "YES" : "NO";
    }

    public static void main(String[] args) {
        assert watermelon(8).equals("YES") && watermelon(2).equals("NO") && watermelon(3).equals("NO");
        System.out.println("4A watermelon ok");
    }
}

import java.util.*;

// Codeforces 339A - Helpful Maths.
public class HelpfulMaths {
    static String helpfulMaths(String expression) {
        String[] parts = expression.split("\\+");
        Arrays.sort(parts);
        return String.join("+", parts);
    }

    public static void main(String[] args) {
        assert helpfulMaths("3+2+1").equals("1+2+3");
        assert helpfulMaths("1+1+3+1+3").equals("1+1+1+3+3");
        System.out.println("339A helpful maths ok");
    }
}

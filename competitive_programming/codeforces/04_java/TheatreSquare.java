import java.util.*;

// Codeforces 1A - Theatre Square.
public class TheatreSquare {
    static long theatreSquare(long n, long m, long a) {
        return ((n + a - 1) / a) * ((m + a - 1) / a);
    }

    public static void main(String[] args) {
        assert theatreSquare(6, 6, 4) == 4 && theatreSquare(1, 1, 1) == 1;
        System.out.println("1A theatre square ok");
    }
}

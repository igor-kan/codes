import java.util.*;

// Codeforces 50A - Domino Piling.
public class DominoPiling {
    static long dominoPiling(long m, long n) {
        return m * n / 2;
    }

    public static void main(String[] args) {
        assert dominoPiling(2, 4) == 4 && dominoPiling(3, 3) == 4;
        System.out.println("50A domino piling ok");
    }
}

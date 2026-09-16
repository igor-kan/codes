import java.util.*;

// Codeforces 977A - Wrong Subtraction.
public class WrongSubtraction {
    static long wrongSubtraction(long number, int steps) {
        for (int i = 0; i < steps; i++) {
            if (number % 10 == 0) number /= 10; else number -= 1;
        }
        return number;
    }

    public static void main(String[] args) {
        assert wrongSubtraction(512, 4) == 50 && wrongSubtraction(1000000000, 9) == 1;
        System.out.println("977A wrong subtraction ok");
    }
}

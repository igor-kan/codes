import java.util.*;

// Codeforces 617A - Elephant.
public class Elephant {
    static int elephant(int position) {
        return (position + 4) / 5;
    }

    public static void main(String[] args) {
        assert elephant(5) == 1 && elephant(12) == 3 && elephant(1) == 1;
        System.out.println("617A elephant ok");
    }
}

import java.util.*;

// Codeforces 282A - Bit++.
public class BitPlusPlus {
    static int bitPlusPlus(String[] operations) {
        int value = 0;
        for (String operation : operations) value += operation.contains("++") ? 1 : -1;
        return value;
    }

    public static void main(String[] args) {
        assert bitPlusPlus(new String[] {"++X", "X++", "--X"}) == 1;
        assert bitPlusPlus(new String[] {"X++", "X++", "X++", "X--"}) == 2;
        System.out.println("282A bit++ ok");
    }
}

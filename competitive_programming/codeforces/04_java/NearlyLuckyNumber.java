import java.util.*;

// Codeforces 110A - Nearly Lucky Number.
public class NearlyLuckyNumber {
    static String nearlyLuckyNumber(long number) {
        int count = 0;
        for (char digit : String.valueOf(number).toCharArray()) if (digit == '4' || digit == '7') count++;
        return count == 4 || count == 7 ? "YES" : "NO";
    }

    public static void main(String[] args) {
        assert nearlyLuckyNumber(47).equals("NO");
        assert nearlyLuckyNumber(7747774).equals("YES");
        assert nearlyLuckyNumber(40047).equals("NO");
        System.out.println("110A nearly lucky number ok");
    }
}

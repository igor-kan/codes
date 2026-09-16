import java.util.*;

// Codeforces 271A - Beautiful Year.
public class BeautifulYear {
    static int beautifulYear(int year) {
        while (true) {
            year++;
            Set<Character> digits = new HashSet<>();
            for (char digit : String.valueOf(year).toCharArray()) digits.add(digit);
            if (digits.size() == 4) return year;
        }
    }

    public static void main(String[] args) {
        assert beautifulYear(1987) == 2013 && beautifulYear(2013) == 2014;
        System.out.println("271A beautiful year ok");
    }
}

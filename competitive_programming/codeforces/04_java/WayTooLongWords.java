import java.util.*;

// Codeforces 71A - Way Too Long Words.
public class WayTooLongWords {
    static String wayTooLong(String word) {
        if (word.length() <= 10) return word;
        return "" + word.charAt(0) + (word.length() - 2) + word.charAt(word.length() - 1);
    }

    public static void main(String[] args) {
        assert wayTooLong("word").equals("word");
        assert wayTooLong("localization").equals("l10n");
        assert wayTooLong("internationalization").equals("i18n");
        System.out.println("71A way too long words ok");
    }
}

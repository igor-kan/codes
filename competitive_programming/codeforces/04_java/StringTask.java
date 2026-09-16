import java.util.*;

// Codeforces 118A - String Task.
public class StringTask {
    static String stringTask(String text) {
        String vowels = "aeiouy";
        StringBuilder builder = new StringBuilder();
        for (char character : text.toLowerCase().toCharArray()) {
            if (vowels.indexOf(character) < 0) builder.append('.').append(character);
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        assert stringTask("Codeforces").equals(".c.d.f.r.c.s");
        assert stringTask("aBAcAba").equals(".b.c.b");
        System.out.println("118A string task ok");
    }
}

import java.util.*;

// Codeforces 136A - Presents.
public class Presents {
    static int[] presents(int[] permutation) {
        int[] result = new int[permutation.length];
        for (int index = 0; index < permutation.length; index++) result[permutation[index] - 1] = index + 1;
        return result;
    }

    public static void main(String[] args) {
        assert Arrays.equals(presents(new int[] {2, 3, 4, 1}), new int[] {4, 1, 2, 3});
        System.out.println("136A presents ok");
    }
}

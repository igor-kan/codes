import java.util.Arrays;

public class SelectionSort {
    public static void sort(int[] a) {
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++)
                if (a[j] < a[min]) min = j;
            int tmp = a[i]; a[i] = a[min]; a[min] = tmp;
        }
    }

    public static void main(String[] args) {
        int[] data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
        sort(data);
        for (int i = 1; i < data.length; i++)
            if (data[i - 1] > data[i]) throw new AssertionError("not sorted at " + i);
        System.out.println("[Java SelectionSort] Selection sort verified: " + Arrays.toString(data));
    }
}

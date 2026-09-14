import java.util.Arrays;

public class InsertionSort {
    public static void sort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int key = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
        sort(data);
        for (int i = 1; i < data.length; i++)
            if (data[i - 1] > data[i]) throw new AssertionError("not sorted at " + i);
        System.out.println("[Java InsertionSort] Insertion sort verified: " + Arrays.toString(data));
    }
}

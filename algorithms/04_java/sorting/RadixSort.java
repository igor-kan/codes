import java.util.Arrays;

public final class RadixSort {
    private RadixSort() {}

    public static void sort(int[] values) {
        if (values.length == 0) return;
        int max = values[0];
        for (int value : values) max = Math.max(max, value);
        int[] buffer = new int[values.length];
        for (int exp = 1; max / exp > 0; exp *= 10) {
            int[] count = new int[10];
            for (int value : values) count[(value / exp) % 10]++;
            for (int i = 1; i < 10; i++) count[i] += count[i - 1];
            for (int i = values.length - 1; i >= 0; i--) {
                int digit = (values[i] / exp) % 10;
                buffer[--count[digit]] = values[i];
            }
            System.arraycopy(buffer, 0, values, 0, values.length);
        }
    }

    public static void main(String[] args) {
        int[] data = {170, 45, 75, 90, 802, 24, 2, 66};
        sort(data);
        int[] expected = data.clone();
        Arrays.sort(expected);
        if (!Arrays.equals(data, expected)) throw new AssertionError("not sorted");
        System.out.println(Arrays.toString(data));
    }
}

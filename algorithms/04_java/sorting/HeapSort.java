public class HeapSort {
    private static void siftDown(int[] a, int root, int end) {
        while (root * 2 + 1 <= end) {
            int swap = root;
            int child = root * 2 + 1;
            if (a[swap] < a[child]) swap = child;
            if (child + 1 <= end && a[swap] < a[child + 1]) swap = child + 1;
            if (swap == root) return;
            int tmp = a[root]; a[root] = a[swap]; a[swap] = tmp;
            root = swap;
        }
    }

    public static void sort(int[] a) {
        int n = a.length;
        if (n <= 1) return;
        for (int start = (n - 2) / 2; start >= 0; start--) siftDown(a, start, n - 1);
        for (int end = n - 1; end > 0; end--) {
            int tmp = a[0]; a[0] = a[end]; a[end] = tmp;
            siftDown(a, 0, end - 1);
        }
    }

    public static void main(String[] args) {
        int[] data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
        sort(data);
        for (int i = 1; i < data.length; i++) {
            if (data[i - 1] > data[i]) throw new AssertionError("not sorted at " + i);
        }
        StringBuilder sb = new StringBuilder("[Java HeapSort] Sift-down heap sort verified: {");
        for (int i = 0; i < data.length; i++) sb.append(data[i]).append(i + 1 < data.length ? ", " : "}");
        System.out.println(sb);
    }
}

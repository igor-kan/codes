import java.util.PriorityQueue;

public final class MaxHeap {
    private MaxHeap() {}

    public static void main(String[] args) {
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        for (int v : new int[] {5, 3, 8, 1, 4}) {
            heap.add(v);
        }
        int prev = Integer.MAX_VALUE;
        while (!heap.isEmpty()) {
            int x = heap.poll();
            if (x > prev) {
                throw new AssertionError("not a max-heap order");
            }
            prev = x;
        }
        System.out.println("max heap ok");
    }
}

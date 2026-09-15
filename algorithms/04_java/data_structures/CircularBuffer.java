public final class CircularBuffer {
    private final int[] data;
    private int head = 0;
    private int size = 0;

    public CircularBuffer(int capacity) {
        data = new int[capacity];
    }

    public void push(int value) {
        data[(head + size) % data.length] = value;
        if (size < data.length) {
            size++;
        } else {
            head = (head + 1) % data.length;
        }
    }

    public int pop() {
        int value = data[head];
        head = (head + 1) % data.length;
        size--;
        return value;
    }

    public static void main(String[] args) {
        CircularBuffer buffer = new CircularBuffer(3);
        for (int i = 1; i <= 4; i++) {
            buffer.push(i);
        }
        if (buffer.pop() != 2 || buffer.pop() != 3 || buffer.pop() != 4) {
            throw new AssertionError("bad overwrite semantics");
        }
        System.out.println("circular buffer ok");
    }
}

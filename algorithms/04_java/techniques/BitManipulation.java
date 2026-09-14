public class BitManipulation {
    public static boolean isPowerOfTwo(int x) { return x > 0 && (x & (x - 1)) == 0; }
    public static int countSetBits(int x) { return Integer.bitCount(x); }
    public static int lowestSetBit(int x) { return x & (-x); }
    public static int clearLowestSetBit(int x) { return x & (x - 1); }
    public static int setBit(int x, int i) { return x | (1 << i); }
    public static boolean testBit(int x, int i) { return (x & (1 << i)) != 0; }
    public static int toggleBit(int x, int i) { return x ^ (1 << i); }

    public static void main(String[] args) {
        if (!isPowerOfTwo(16)) throw new AssertionError("16 is power of two");
        if (isPowerOfTwo(18)) throw new AssertionError("18 is not power of two");
        if (countSetBits(0b10110) != 3) throw new AssertionError("popcount should be 3");
        if (lowestSetBit(0b10100) != 4) throw new AssertionError("lowest set bit should be 4");
        if (clearLowestSetBit(0b10100) != 0b10000) throw new AssertionError("clear lowest bit failed");
        if (setBit(0b100, 1) != 0b110) throw new AssertionError("setBit failed");
        if (!testBit(0b100, 2)) throw new AssertionError("testBit failed");
        if (toggleBit(0b101, 1) != 0b111) throw new AssertionError("toggleBit failed");
        System.out.println("[Java BitManipulation] Bit tricks verified");
    }
}

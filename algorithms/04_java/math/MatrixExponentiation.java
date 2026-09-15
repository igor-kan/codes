public final class MatrixExponentiation {
    private MatrixExponentiation() {}

    private static long[][] multiply(long[][] a, long[][] b) {
        long[][] r = new long[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    r[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return r;
    }

    public static long fib(int n) {
        long[][] result = {{1, 0}, {0, 1}};
        long[][] base = {{1, 1}, {1, 0}};
        while (n > 0) {
            if ((n & 1) == 1) {
                result = multiply(result, base);
            }
            base = multiply(base, base);
            n >>= 1;
        }
        return result[0][1];
    }

    public static void main(String[] args) {
        if (fib(10) != 55 || fib(20) != 6765) {
            throw new AssertionError("wrong Fibonacci");
        }
        System.out.println("fib(20)=" + fib(20));
    }
}

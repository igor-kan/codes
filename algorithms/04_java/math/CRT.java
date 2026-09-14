public class CRT {
    // Solves x = rem[i] (mod mod[i]) for pairwise coprime moduli.
    public static long crt(long[] rem, long[] mod) {
        long prod = 1;
        for (long m : mod) prod *= m;
        long result = 0;
        for (int i = 0; i < rem.length; i++) {
            long pp = prod / mod[i];
            result += rem[i] * modInverse(pp, mod[i]) * pp;
            result %= prod;
        }
        return (result + prod) % prod;
    }

    private static long modInverse(long a, long m) {
        long[] r = extendedEuclid(a, m);
        if (r[0] != 1) throw new ArithmeticException("inverse does not exist");
        return (r[1] % m + m) % m;
    }

    private static long[] extendedEuclid(long a, long b) {
        if (b == 0) return new long[]{a, 1, 0};
        long[] r = extendedEuclid(b, a % b);
        return new long[]{r[0], r[2], r[1] - (a / b) * r[2]};
    }

    public static void main(String[] args) {
        long[] rem = {2, 3, 2};
        long[] mod = {3, 5, 7};
        long x = crt(rem, mod);
        if (x != 23) throw new AssertionError("CRT solution should be 23, got " + x);
        for (int i = 0; i < rem.length; i++)
            if (x % mod[i] != rem[i]) throw new AssertionError("CRT wrong for modulus " + mod[i]);
        System.out.println("[Java CRT] Chinese Remainder Theorem verified: x = " + x);
    }
}

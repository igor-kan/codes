public class ModInverse {
    public static long modPow(long base, long exp, long mod) {
        long r = 1;
        base %= mod;
        for (; exp > 0; exp >>= 1) {
            if ((exp & 1) == 1) r = r * base % mod;
            base = base * base % mod;
        }
        return r;
    }

    // Returns {gcd, x, y} such that a*x + b*y = gcd.
    public static long[] extendedEuclid(long a, long b) {
        if (b == 0) return new long[]{a, 1, 0};
        long[] r = extendedEuclid(b, a % b);
        long g = r[0], x1 = r[1], y1 = r[2];
        return new long[]{g, y1, x1 - (a / b) * y1};
    }

    public static long modInverseEuclid(long a, long mod) {
        long[] r = extendedEuclid(a % mod, mod);
        if (r[0] != 1) throw new ArithmeticException("inverse does not exist");
        long inv = r[1] % mod;
        if (inv < 0) inv += mod;
        return inv;
    }

    public static long modInverseFermat(long a, long mod) {
        return modPow(a, mod - 2, mod);
    }

    public static void main(String[] args) {
        long mod = 1_000_000_007L;
        long a = 123456789L;
        long invE = modInverseEuclid(a, mod);
        long invF = modInverseFermat(a, mod);
        if (invE != invF) throw new AssertionError("Euclid and Fermat inverses differ");
        if (a * invE % mod != 1) throw new AssertionError("a * inv != 1 (mod)");
        System.out.println("[Java ModInverse] Modular inverse (Euclid + Fermat) verified");
    }
}

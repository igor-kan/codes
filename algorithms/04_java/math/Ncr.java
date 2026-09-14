public class Ncr {
    private static final long MOD = 1_000_000_007L;

    public static long modPow(long base, long exp, long mod) {
        long r = 1;
        base %= mod;
        for (; exp > 0; exp >>= 1) {
            if ((exp & 1) == 1) r = r * base % mod;
            base = base * base % mod;
        }
        return r;
    }

    public static long ncr(long[] fact, long[] invFact, int n, int r) {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    }

    public static void main(String[] args) {
        int maxN = 100;
        long[] fact = new long[maxN + 1];
        long[] invFact = new long[maxN + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxN; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxN] = modPow(fact[maxN], MOD - 2, MOD);
        for (int i = maxN; i >= 1; i--) invFact[i - 1] = invFact[i] * i % MOD;

        if (ncr(fact, invFact, 10, 3) != 120) throw new AssertionError("C(10,3) should be 120");
        if (ncr(fact, invFact, 5, 5) != 1) throw new AssertionError("C(5,5) should be 1");
        if (ncr(fact, invFact, 5, 6) != 0) throw new AssertionError("C(5,6) should be 0");
        System.out.println("[Java Ncr] nCr mod p verified");
    }
}

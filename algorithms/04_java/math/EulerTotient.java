public class EulerTotient {
    public static int phi(int n) {
        int result = n;
        for (int p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                while (n % p == 0) n /= p;
                result -= result / p;
            }
        }
        if (n > 1) result -= result / n;
        return result;
    }

    public static int[] phiUpTo(int n) {
        int[] phi = new int[n + 1];
        for (int i = 0; i <= n; i++) phi[i] = i;
        for (int p = 2; p <= n; p++) {
            if (phi[p] == p) {
                for (int j = p; j <= n; j += p) phi[j] -= phi[j] / p;
            }
        }
        return phi;
    }

    public static void main(String[] args) {
        if (phi(1) != 1) throw new AssertionError("phi(1) should be 1");
        if (phi(12) != 4) throw new AssertionError("phi(12) should be 4");
        if (phi(17) != 16) throw new AssertionError("phi(17) should be 16");
        int[] p = phiUpTo(20);
        if (p[12] != 4 || p[17] != 16) throw new AssertionError("sieve totient mismatch");
        System.out.println("[Java EulerTotient] Euler's totient verified");
    }
}

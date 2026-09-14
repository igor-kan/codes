using System;

namespace Algorithms.Maths
{
    public static class BinomialCoefficient
    {
        public static long NChooseR(int n, int r, long mod)
        {
            if (r < 0 || r > n) return 0;
            var fact = new long[n + 1];
            var invFact = new long[n + 1];
            fact[0] = 1;
            for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % mod;
            invFact[n] = ModularExponentiation(fact[n], mod - 2, mod);
            for (int i = n; i >= 1; i--) invFact[i - 1] = invFact[i] * i % mod;
            return fact[n] * invFact[r] % mod * invFact[n - r] % mod;
        }

        private static long ModularExponentiation(long b, long e, long mod)
        {
            long result = 1;
            b %= mod;
            while (e > 0)
            {
                if ((e & 1) == 1) result = result * b % mod;
                b = b * b % mod;
                e >>= 1;
            }
            return result;
        }

        public static void Main()
        {
            bool ok = NChooseR(5, 2, 1000000007) == 10 && NChooseR(10, 0, 1000000007) == 1;
            Console.WriteLine(ok ? "[C# BinomialCoefficient] ... verified" : "[C# BinomialCoefficient] ... FAILED");
        }
    }
}

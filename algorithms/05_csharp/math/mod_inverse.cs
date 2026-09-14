using System;

namespace Algorithms.Maths
{
    public static class ModularInverse
    {
        public static long Inverse(long a, long mod)
        {
            a %= mod;
            if (Gcd(a, mod) != 1) return -1;
            ExtendedGcd(a, mod, out long x, out long _);
            return ((x % mod) + mod) % mod;
        }

        private static long Gcd(long a, long b)
        {
            while (b != 0)
            {
                long t = b;
                b = a % b;
                a = t;
            }
            return a;
        }

        private static void ExtendedGcd(long a, long b, out long x, out long y)
        {
            if (b == 0)
            {
                x = 1;
                y = 0;
                return;
            }
            ExtendedGcd(b, a % b, out long x1, out long y1);
            x = y1;
            y = x1 - (a / b) * y1;
        }

        public static void Main()
        {
            bool ok = (3 * Inverse(3, 1000000007)) % 1000000007 == 1;
            Console.WriteLine(ok ? "[C# ModularInverse] ... verified" : "[C# ModularInverse] ... FAILED");
        }
    }
}

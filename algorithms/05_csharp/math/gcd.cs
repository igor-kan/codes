namespace Algorithms.Maths
{
    public static class NumberTheory
    {
        public static long Gcd(long a, long b)
        {
            while (b != 0)
            {
                long temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }

        public static long Lcm(long a, long b) => (a / Gcd(a, b)) * b;
    }
}

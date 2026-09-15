using System;

namespace Algorithms.Math
{
    public static class MatrixExponentiation
    {
        private static long[,] Multiply(long[,] a, long[,] b)
        {
            var r = new long[2, 2];
            for (int i = 0; i < 2; i++)
            {
                for (int j = 0; j < 2; j++)
                {
                    for (int k = 0; k < 2; k++)
                    {
                        r[i, j] += a[i, k] * b[k, j];
                    }
                }
            }
            return r;
        }

        public static long Fib(int n)
        {
            var result = new long[,] { { 1, 0 }, { 0, 1 } };
            var m = new long[,] { { 1, 1 }, { 1, 0 } };
            while (n > 0)
            {
                if ((n & 1) == 1) result = Multiply(result, m);
                m = Multiply(m, m);
                n >>= 1;
            }
            return result[0, 1];
        }

        public static void Main()
        {
            if (Fib(10) != 55 || Fib(20) != 6765)
            {
                throw new InvalidOperationException("wrong Fibonacci");
            }
            Console.WriteLine($"fib(20)={Fib(20)}");
        }
    }
}

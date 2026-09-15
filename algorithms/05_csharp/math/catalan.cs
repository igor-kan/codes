using System;

namespace Algorithms.Math
{
    public static class Catalan
    {
        public static void Main()
        {
            var catalan = new long[11];
            catalan[0] = 1;
            for (int i = 1; i <= 10; i++)
            {
                long sum = 0;
                for (int j = 0; j < i; j++)
                {
                    sum += catalan[j] * catalan[i - 1 - j];
                }
                catalan[i] = sum;
            }
            if (catalan[5] != 42 || catalan[10] != 16796)
            {
                throw new InvalidOperationException("wrong Catalan numbers");
            }
            Console.WriteLine($"catalan(10)={catalan[10]}");
        }
    }
}

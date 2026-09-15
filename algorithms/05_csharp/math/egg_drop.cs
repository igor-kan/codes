using System;

namespace Algorithms.Math
{
    public static class EggDrop
    {
        public static void Main()
        {
            const int eggs = 2;
            const int floors = 100;
            var dp = new int[101, eggs + 1];
            int trials = 0;
            while (dp[trials, eggs] < floors)
            {
                trials++;
                for (int k = 1; k <= eggs; k++)
                {
                    dp[trials, k] = dp[trials - 1, k - 1] + dp[trials - 1, k] + 1;
                }
            }
            if (trials != 14)
            {
                throw new InvalidOperationException("expected 14 trials");
            }
            Console.WriteLine($"egg drop={trials}");
        }
    }
}

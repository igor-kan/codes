using System;

namespace Algorithms.DynamicProgramming
{
    public static class Knapsack
    {
        public static int Solve(int[] weights, int[] values, int capacity)
        {
            int n = weights.Length;
            int[] dp = new int[capacity + 1];

            for (int i = 0; i < n; i++)
            {
                for (int w = capacity; w >= weights[i]; w--)
                {
                    dp[w] = Math.Max(dp[w], dp[w - weights[i]] + values[i]);
                }
            }

            return dp[capacity];
        }
    }
}

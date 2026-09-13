using System;

public class Knapsack
{
    public static int SolveKnapsack(int[] weights, int[] values, int capacity)
    {
        int n = weights.Length;
        int[] dp = new int[capacity + 1];

        for (int i = 0; i < n; i++)
        {
            int w = weights[i];
            int v = values[i];
            for (int cap = capacity; cap >= w; cap--)
            {
                dp[cap] = Math.Max(dp[cap], dp[cap - w] + v);
            }
        }
        return dp[capacity];
    }

    public static void Main(string[] args)
    {
        int[] weights = { 2, 3, 4, 5 };
        int[] values = { 3, 4, 5, 6 };
        int capacity = 5;

        int maxVal = SolveKnapsack(weights, values, capacity);
        Console.WriteLine($"[C# Knapsack] Capacity 5 -> Max Value: {maxVal}");
        if (maxVal != 7) throw new Exception("Knapsack assertion failed");
    }
}

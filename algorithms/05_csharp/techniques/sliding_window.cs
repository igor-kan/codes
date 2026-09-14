using System;

namespace Algorithms.Techniques
{
    public static class SlidingWindow
    {
        public static int MaxSumSubarray(int[] array, int k)
        {
            if (k <= 0 || array.Length < k) return 0;
            int windowSum = 0;
            for (int i = 0; i < k; i++) windowSum += array[i];
            int maxSum = windowSum;
            for (int i = k; i < array.Length; i++)
            {
                windowSum += array[i] - array[i - k];
                maxSum = Math.Max(maxSum, windowSum);
            }
            return maxSum;
        }

        public static void Main()
        {
            int[] a = { 2, 1, 5, 1, 3, 2 };
            bool ok = MaxSumSubarray(a, 3) == 9;
            Console.WriteLine(ok ? "[C# SlidingWindow] ... verified" : "[C# SlidingWindow] ... FAILED");
        }
    }
}

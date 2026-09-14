using System;

namespace Algorithms.DynamicProgramming
{
    public static class Kadane
    {
        public static int MaxSubarraySum(int[] array)
        {
            int best = array[0], current = array[0];
            for (int i = 1; i < array.Length; i++)
            {
                current = Math.Max(array[i], current + array[i]);
                best = Math.Max(best, current);
            }
            return best;
        }

        public static void Main()
        {
            int[] a = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
            bool ok = MaxSubarraySum(a) == 6;
            Console.WriteLine(ok ? "[C# Kadane] ... verified" : "[C# Kadane] ... FAILED");
        }
    }
}

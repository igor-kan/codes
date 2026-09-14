using System;
using System.Collections.Generic;

namespace Algorithms.DynamicProgramming
{
    public static class LongestIncreasingSubsequence
    {
        public static int Length(int[] array)
        {
            var tails = new List<int>();
            foreach (int x in array)
            {
                int idx = tails.BinarySearch(x);
                if (idx < 0) idx = ~idx;
                if (idx == tails.Count) tails.Add(x);
                else tails[idx] = x;
            }
            return tails.Count;
        }

        public static void Main()
        {
            int[] a = { 10, 9, 2, 5, 3, 7, 101, 18 };
            bool ok = Length(a) == 4;
            Console.WriteLine(ok ? "[C# LongestIncreasingSubsequence] ... verified" : "[C# LongestIncreasingSubsequence] ... FAILED");
        }
    }
}

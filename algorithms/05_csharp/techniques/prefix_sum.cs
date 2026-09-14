using System;

namespace Algorithms.Techniques
{
    public static class PrefixSum
    {
        public static long[] Build(int[] array)
        {
            var prefix = new long[array.Length + 1];
            for (int i = 0; i < array.Length; i++)
                prefix[i + 1] = prefix[i] + array[i];
            return prefix;
        }

        public static long RangeSum(long[] prefix, int left, int right)
        {
            return prefix[right + 1] - prefix[left];
        }

        public static void Main()
        {
            var prefix = Build(new[] { 3, 1, 4, 1, 5, 9 });
            bool ok = RangeSum(prefix, 0, 2) == 8 && RangeSum(prefix, 2, 4) == 10 && RangeSum(prefix, 1, 3) == 6;
            Console.WriteLine(ok ? "[C# PrefixSum] ... verified" : "[C# PrefixSum] ... FAILED");
        }
    }
}

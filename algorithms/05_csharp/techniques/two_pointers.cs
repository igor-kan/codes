using System;

namespace Algorithms.Techniques
{
    public static class TwoPointers
    {
        public static bool HasPairWithSum(int[] sorted, int target)
        {
            int left = 0, right = sorted.Length - 1;
            while (left < right)
            {
                int sum = sorted[left] + sorted[right];
                if (sum == target) return true;
                if (sum < target) left++;
                else right--;
            }
            return false;
        }

        public static void Main()
        {
            int[] a = { 1, 2, 3, 4, 5, 6 };
            bool ok = HasPairWithSum(a, 9) && !HasPairWithSum(a, 15);
            Console.WriteLine(ok ? "[C# TwoPointers] ... verified" : "[C# TwoPointers] ... FAILED");
        }
    }
}

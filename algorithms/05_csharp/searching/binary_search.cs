using System;

namespace Algorithms.Searching
{
    public static class BinarySearch
    {
        public static int LowerBound(int[] array, int target)
        {
            int lo = 0, hi = array.Length;
            while (lo < hi)
            {
                int mid = lo + (hi - lo) / 2;
                if (array[mid] < target) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }

        public static int UpperBound(int[] array, int target)
        {
            int lo = 0, hi = array.Length;
            while (lo < hi)
            {
                int mid = lo + (hi - lo) / 2;
                if (array[mid] <= target) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }

        public static void Main()
        {
            int[] a = { 1, 2, 2, 2, 3, 5 };
            bool ok = LowerBound(a, 2) == 1 && UpperBound(a, 2) == 4 && LowerBound(a, 4) == 5;
            Console.WriteLine(ok ? "[C# BinarySearch] ... verified" : "[C# BinarySearch] ... FAILED");
        }
    }
}

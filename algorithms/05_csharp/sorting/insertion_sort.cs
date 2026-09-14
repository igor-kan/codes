using System;

namespace Algorithms.Sorting
{
    public static class InsertionSort
    {
        public static void Sort<T>(T[] array) where T : IComparable<T>
        {
            int n = array.Length;
            for (int i = 1; i < n; i++)
            {
                T key = array[i];
                int j = i - 1;
                while (j >= 0 && array[j].CompareTo(key) > 0)
                {
                    array[j + 1] = array[j];
                    j--;
                }
                array[j + 1] = key;
            }
        }

        public static void Main()
        {
            int[] a = { 5, 2, 4, 6, 1, 3 };
            Sort(a);
            bool ok = a[0] == 1 && a[5] == 6;
            Console.WriteLine(ok ? "[C# InsertionSort] ... verified" : "[C# InsertionSort] ... FAILED");
        }
    }
}

using System;

namespace Algorithms.Sorting
{
    public static class SelectionSort
    {
        public static void Sort<T>(T[] array) where T : IComparable<T>
        {
            int n = array.Length;
            for (int i = 0; i < n - 1; i++)
            {
                int minIndex = i;
                for (int j = i + 1; j < n; j++)
                {
                    if (array[j].CompareTo(array[minIndex]) < 0)
                        minIndex = j;
                }
                (array[i], array[minIndex]) = (array[minIndex], array[i]);
            }
        }

        public static void Main()
        {
            int[] a = { 64, 25, 12, 22, 11 };
            Sort(a);
            bool ok = a[0] == 11 && a[4] == 64;
            Console.WriteLine(ok ? "[C# SelectionSort] ... verified" : "[C# SelectionSort] ... FAILED");
        }
    }
}

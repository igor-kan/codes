using System;

namespace Algorithms.Sorting
{
    public static class QuickSort
    {
        public static void Sort<T>(T[] array, int low, int high) where T : IComparable<T>
        {
            if (low < high)
            {
                int pivotIndex = Partition(array, low, high);
                Sort(array, low, pivotIndex - 1);
                Sort(array, pivotIndex + 1, high);
            }
        }

        private static int Partition<T>(T[] array, int low, int high) where T : IComparable<T>
        {
            T pivot = array[high];
            int i = low - 1;
            for (int j = low; j < high; j++)
            {
                if (array[j].CompareTo(pivot) <= 0)
                {
                    i++;
                    (array[i], array[j]) = (array[j], array[i]);
                }
            }
            (array[i + 1], array[high]) = (array[high], array[i + 1]);
            return i + 1;
        }
    }
}

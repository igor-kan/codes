using System;

namespace Algorithms.Sorting
{
    public static class MergeSort
    {
        public static void Sort<T>(T[] array, int left, int right) where T : IComparable<T>
        {
            if (left < right)
            {
                int mid = left + (right - left) / 2;
                Sort(array, left, mid);
                Sort(array, mid + 1, right);
                Merge(array, left, mid, right);
            }
        }

        private static void Merge<T>(T[] array, int left, int mid, int right) where T : IComparable<T>
        {
            int n1 = mid - left + 1;
            int n2 = right - mid;
            T[] L = new T[n1];
            T[] R = new T[n2];

            Array.Copy(array, left, L, 0, n1);
            Array.Copy(array, mid + 1, R, 0, n2);

            int i = 0, j = 0, k = left;
            while (i < n1 && j < n2)
            {
                if (L[i].CompareTo(R[j]) <= 0)
                    array[k++] = L[i++];
                else
                    array[k++] = R[j++];
            }

            while (i < n1) array[k++] = L[i++];
            while (j < n2) array[k++] = R[j++];
        }
    }
}

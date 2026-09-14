using System;

namespace Algorithms.DataStructures
{
    public class SparseTable
    {
        private readonly int[,] _table;
        private readonly int[] _log;

        public SparseTable(int[] values)
        {
            int n = values.Length;
            _log = new int[n + 1];
            for (int i = 2; i <= n; i++) _log[i] = _log[i / 2] + 1;

            int k = _log[n] + 1;
            _table = new int[n, k];
            for (int i = 0; i < n; i++) _table[i, 0] = values[i];

            for (int j = 1; j < k; j++)
            {
                for (int i = 0; i + (1 << j) - 1 < n; i++)
                {
                    _table[i, j] = Math.Min(_table[i, j - 1], _table[i + (1 << (j - 1)), j - 1]);
                }
            }
        }

        public int RangeMin(int left, int right)
        {
            int j = _log[right - left + 1];
            return Math.Min(_table[left, j], _table[right - (1 << j) + 1, j]);
        }

        public static void Main()
        {
            var st = new SparseTable(new[] { 4, 2, 7, 1, 9, 3, 6 });
            bool ok = st.RangeMin(0, 6) == 1 && st.RangeMin(2, 4) == 1 && st.RangeMin(0, 2) == 2;
            Console.WriteLine(ok ? "[C# SparseTable] ... verified" : "[C# SparseTable] ... FAILED");
        }
    }
}

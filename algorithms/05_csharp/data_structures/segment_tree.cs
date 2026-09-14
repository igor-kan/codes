using System;

namespace Algorithms.DataStructures
{
    public class SegmentTree
    {
        private readonly int _n;
        private readonly long[] _tree;

        public SegmentTree(int[] values)
        {
            _n = values.Length;
            _tree = new long[4 * _n];
            Build(values, 1, 0, _n - 1);
        }

        private void Build(int[] values, int node, int left, int right)
        {
            if (left == right)
            {
                _tree[node] = values[left];
                return;
            }
            int mid = left + (right - left) / 2;
            Build(values, 2 * node, left, mid);
            Build(values, 2 * node + 1, mid + 1, right);
            _tree[node] = _tree[2 * node] + _tree[2 * node + 1];
        }

        public void Update(int index, int value) => Update(1, 0, _n - 1, index, value);

        private void Update(int node, int left, int right, int index, int value)
        {
            if (left == right)
            {
                _tree[node] = value;
                return;
            }
            int mid = left + (right - left) / 2;
            if (index <= mid) Update(2 * node, left, mid, index, value);
            else Update(2 * node + 1, mid + 1, right, index, value);
            _tree[node] = _tree[2 * node] + _tree[2 * node + 1];
        }

        public long Query(int ql, int qr) => Query(1, 0, _n - 1, ql, qr);

        private long Query(int node, int left, int right, int ql, int qr)
        {
            if (qr < left || right < ql) return 0;
            if (ql <= left && right <= qr) return _tree[node];
            int mid = left + (right - left) / 2;
            return Query(2 * node, left, mid, ql, qr) + Query(2 * node + 1, mid + 1, right, ql, qr);
        }

        public static void Main()
        {
            var st = new SegmentTree(new[] { 1, 3, 5, 7, 9, 11 });
            st.Update(2, 10);
            bool ok = st.Query(1, 4) == 29 && st.Query(0, 5) == 41;
            Console.WriteLine(ok ? "[C# SegmentTree] ... verified" : "[C# SegmentTree] ... FAILED");
        }
    }
}

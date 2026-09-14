using System;

namespace Algorithms.DataStructures
{
    public class DisjointSetUnion
    {
        private readonly int[] _parent;
        private readonly int[] _rank;

        public DisjointSetUnion(int n)
        {
            _parent = new int[n];
            _rank = new int[n];
            for (int i = 0; i < n; i++) _parent[i] = i;
        }

        public int Find(int x)
        {
            if (_parent[x] != x)
                _parent[x] = Find(_parent[x]);
            return _parent[x];
        }

        public void Union(int x, int y)
        {
            int rx = Find(x), ry = Find(y);
            if (rx == ry) return;
            if (_rank[rx] < _rank[ry])
                (rx, ry) = (ry, rx);
            _parent[ry] = rx;
            if (_rank[rx] == _rank[ry]) _rank[rx]++;
        }

        public bool Connected(int x, int y) => Find(x) == Find(y);

        public static void Main()
        {
            var dsu = new DisjointSetUnion(5);
            dsu.Union(0, 1);
            dsu.Union(1, 2);
            dsu.Union(3, 4);
            bool ok = dsu.Connected(0, 2) && dsu.Connected(3, 4) && !dsu.Connected(0, 3);
            Console.WriteLine(ok ? "[C# DisjointSetUnion] ... verified" : "[C# DisjointSetUnion] ... FAILED");
        }
    }
}

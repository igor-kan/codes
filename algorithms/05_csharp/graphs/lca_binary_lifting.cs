using System;
using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public class LowestCommonAncestor
    {
        private readonly int _n;
        private readonly int _log;
        private readonly int[,] _up;
        private readonly int[] _depth;

        public LowestCommonAncestor(int n, List<(int from, int to)> edges, int root = 0)
        {
            _n = n;
            _log = (int)Math.Ceiling(Math.Log2(n)) + 1;
            _up = new int[n, _log];
            _depth = new int[n];

            var graph = new List<int>[n];
            for (int i = 0; i < n; i++) graph[i] = new List<int>();
            foreach (var (u, v) in edges)
            {
                graph[u].Add(v);
                graph[v].Add(u);
            }

            var visited = new bool[n];
            Dfs(root, root, graph, visited);
        }

        private void Dfs(int u, int parent, List<int>[] graph, bool[] visited)
        {
            visited[u] = true;
            _up[u, 0] = parent;
            for (int j = 1; j < _log; j++)
                _up[u, j] = _up[_up[u, j - 1], j - 1];

            foreach (int v in graph[u])
            {
                if (!visited[v])
                {
                    _depth[v] = _depth[u] + 1;
                    Dfs(v, u, graph, visited);
                }
            }
        }

        public int Query(int a, int b)
        {
            if (_depth[a] < _depth[b]) (a, b) = (b, a);

            int diff = _depth[a] - _depth[b];
            for (int j = 0; j < _log; j++)
                if ((diff & (1 << j)) != 0) a = _up[a, j];

            if (a == b) return a;

            for (int j = _log - 1; j >= 0; j--)
            {
                if (_up[a, j] != _up[b, j])
                {
                    a = _up[a, j];
                    b = _up[b, j];
                }
            }
            return _up[a, 0];
        }

        public static void Main()
        {
            var edges = new List<(int, int)> { (0, 1), (0, 2), (1, 3), (1, 4), (2, 5) };
            var lca = new LowestCommonAncestor(6, edges);
            bool ok = lca.Query(3, 4) == 1 && lca.Query(3, 5) == 0 && lca.Query(3, 1) == 1;
            Console.WriteLine(ok ? "[C# LowestCommonAncestor] ... verified" : "[C# LowestCommonAncestor] ... FAILED");
        }
    }
}

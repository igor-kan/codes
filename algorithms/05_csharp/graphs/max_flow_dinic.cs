using System;
using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public class MaxFlowDinic
    {
        private readonly int _n;
        private readonly List<int>[] _graph;
        private readonly List<Edge> _edges = new();
        private int[] _level;
        private int[] _iter;

        private sealed class Edge
        {
            public int To;
            public long Capacity;
            public int Reverse;

            public Edge(int to, long capacity, int reverse)
            {
                To = to;
                Capacity = capacity;
                Reverse = reverse;
            }
        }

        public MaxFlowDinic(int n)
        {
            _n = n;
            _graph = new List<int>[n];
            for (int i = 0; i < n; i++) _graph[i] = new List<int>();
        }

        public void AddEdge(int from, int to, long capacity)
        {
            _graph[from].Add(_edges.Count);
            _edges.Add(new Edge(to, capacity, _edges.Count + 1));
            _graph[to].Add(_edges.Count);
            _edges.Add(new Edge(from, 0, _edges.Count - 1));
        }

        public long MaxFlow(int source, int sink)
        {
            long flow = 0;
            while (Bfs(source, sink))
            {
                _iter = new int[_n];
                long f;
                while ((f = Dfs(source, sink, long.MaxValue)) > 0)
                    flow += f;
            }
            return flow;
        }

        private bool Bfs(int source, int sink)
        {
            _level = new int[_n];
            Array.Fill(_level, -1);
            var queue = new Queue<int>();
            _level[source] = 0;
            queue.Enqueue(source);

            while (queue.Count > 0)
            {
                int u = queue.Dequeue();
                foreach (int idx in _graph[u])
                {
                    var e = _edges[idx];
                    if (e.Capacity > 0 && _level[e.To] < 0)
                    {
                        _level[e.To] = _level[u] + 1;
                        queue.Enqueue(e.To);
                    }
                }
            }

            return _level[sink] >= 0;
        }

        private long Dfs(int u, int sink, long pushed)
        {
            if (u == sink) return pushed;
            for (; _iter[u] < _graph[u].Count; _iter[u]++)
            {
                int idx = _graph[u][_iter[u]];
                var e = _edges[idx];
                if (e.Capacity > 0 && _level[u] < _level[e.To])
                {
                    long tr = Dfs(e.To, sink, Math.Min(pushed, e.Capacity));
                    if (tr > 0)
                    {
                        _edges[idx].Capacity -= tr;
                        _edges[e.Reverse].Capacity += tr;
                        return tr;
                    }
                }
            }
            return 0;
        }

        public static void Main()
        {
            var dinic = new MaxFlowDinic(6);
            dinic.AddEdge(0, 1, 10);
            dinic.AddEdge(0, 2, 10);
            dinic.AddEdge(1, 2, 2);
            dinic.AddEdge(1, 3, 4);
            dinic.AddEdge(1, 4, 8);
            dinic.AddEdge(2, 4, 9);
            dinic.AddEdge(3, 5, 10);
            dinic.AddEdge(4, 3, 6);
            dinic.AddEdge(4, 5, 10);
            bool ok = dinic.MaxFlow(0, 5) == 19;
            Console.WriteLine(ok ? "[C# MaxFlowDinic] ... verified" : "[C# MaxFlowDinic] ... FAILED");
        }
    }
}

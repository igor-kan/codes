using System;
using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public static class KahnTopologicalSort
    {
        public static List<int> TopologicalOrder(int n, List<(int from, int to)> edges)
        {
            var graph = new List<int>[n];
            for (int i = 0; i < n; i++) graph[i] = new List<int>();
            var indegree = new int[n];
            foreach (var (from, to) in edges)
            {
                graph[from].Add(to);
                indegree[to]++;
            }

            var queue = new Queue<int>();
            for (int i = 0; i < n; i++)
                if (indegree[i] == 0) queue.Enqueue(i);

            var order = new List<int>();
            while (queue.Count > 0)
            {
                int u = queue.Dequeue();
                order.Add(u);
                foreach (int v in graph[u])
                {
                    if (--indegree[v] == 0) queue.Enqueue(v);
                }
            }

            return order.Count == n ? order : new List<int>();
        }

        public static void Main()
        {
            var edges = new List<(int, int)> { (5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1) };
            var order = TopologicalOrder(6, edges);
            var pos = new Dictionary<int, int>();
            for (int i = 0; i < order.Count; i++) pos[order[i]] = i;
            bool ok = order.Count == 6;
            foreach (var (u, v) in edges) ok &= pos[u] < pos[v];
            Console.WriteLine(ok ? "[C# KahnTopologicalSort] ... verified" : "[C# KahnTopologicalSort] ... FAILED");
        }
    }
}

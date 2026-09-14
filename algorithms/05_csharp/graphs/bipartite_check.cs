using System;
using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public static class BipartiteCheck
    {
        public static bool IsBipartite(int n, List<(int from, int to)> edges)
        {
            var graph = new List<int>[n];
            for (int i = 0; i < n; i++) graph[i] = new List<int>();
            foreach (var (u, v) in edges)
            {
                graph[u].Add(v);
                graph[v].Add(u);
            }

            var color = new int[n];
            Array.Fill(color, -1);

            for (int start = 0; start < n; start++)
            {
                if (color[start] != -1) continue;
                var queue = new Queue<int>();
                color[start] = 0;
                queue.Enqueue(start);

                while (queue.Count > 0)
                {
                    int u = queue.Dequeue();
                    foreach (int v in graph[u])
                    {
                        if (color[v] == -1)
                        {
                            color[v] = color[u] ^ 1;
                            queue.Enqueue(v);
                        }
                        else if (color[v] == color[u])
                        {
                            return false;
                        }
                    }
                }
            }

            return true;
        }

        public static void Main()
        {
            var even = new List<(int, int)> { (0, 1), (1, 2), (2, 3), (3, 0) };
            var odd = new List<(int, int)> { (0, 1), (1, 2), (2, 0) };
            bool ok = IsBipartite(4, even) && !IsBipartite(3, odd);
            Console.WriteLine(ok ? "[C# BipartiteCheck] ... verified" : "[C# BipartiteCheck] ... FAILED");
        }
    }
}

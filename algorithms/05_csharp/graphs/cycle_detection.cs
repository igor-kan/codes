using System;
using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public static class CycleDetection
    {
        public static bool HasCycle(int n, List<(int from, int to)> edges)
        {
            var graph = new List<int>[n];
            for (int i = 0; i < n; i++) graph[i] = new List<int>();
            foreach (var (u, v) in edges) graph[u].Add(v);

            var state = new int[n];
            for (int i = 0; i < n; i++)
            {
                if (state[i] == 0 && Dfs(i, graph, state))
                    return true;
            }
            return false;
        }

        private static bool Dfs(int u, List<int>[] graph, int[] state)
        {
            state[u] = 1;
            foreach (int v in graph[u])
            {
                if (state[v] == 1) return true;
                if (state[v] == 0 && Dfs(v, graph, state)) return true;
            }
            state[u] = 2;
            return false;
        }

        public static void Main()
        {
            var withCycle = new List<(int, int)> { (0, 1), (1, 2), (2, 0) };
            var acyclic = new List<(int, int)> { (0, 1), (1, 2), (0, 2) };
            bool ok = HasCycle(3, withCycle) && !HasCycle(3, acyclic);
            Console.WriteLine(ok ? "[C# CycleDetection] ... verified" : "[C# CycleDetection] ... FAILED");
        }
    }
}

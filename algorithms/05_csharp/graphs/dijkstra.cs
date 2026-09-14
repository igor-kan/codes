using System;
using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public static class Dijkstra
    {
        public static Dictionary<int, long> ShortestPaths(Dictionary<int, List<(int target, long weight)>> graph, int source)
        {
            var distances = new Dictionary<int, long> { [source] = 0 };
            var pq = new PriorityQueue<int, long>();
            pq.Enqueue(source, 0);

            while (pq.Count > 0)
            {
                pq.TryDequeue(out int u, out long currentDist);

                if (currentDist > distances[u]) continue;

                if (graph.TryGetValue(u, out var edges))
                {
                    foreach (var (v, weight) in edges)
                    {
                        long newDist = currentDist + weight;
                        if (!distances.ContainsKey(v) || newDist < distances[v])
                        {
                            distances[v] = newDist;
                            pq.Enqueue(v, newDist);
                        }
                    }
                }
            }

            return distances;
        }
    }
}

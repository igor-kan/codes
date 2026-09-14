using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public static class BreadthFirstSearch
    {
        public static List<int> Traverse(Dictionary<int, List<int>> graph, int start)
        {
            var visited = new HashSet<int>();
            var queue = new Queue<int>();
            var order = new List<int>();

            visited.Add(start);
            queue.Enqueue(start);

            while (queue.Count > 0)
            {
                int node = queue.Dequeue();
                order.Add(node);

                if (graph.TryGetValue(node, out var neighbors))
                {
                    foreach (var neighbor in neighbors)
                    {
                        if (visited.Add(neighbor))
                        {
                            queue.Enqueue(neighbor);
                        }
                    }
                }
            }

            return order;
        }
    }
}

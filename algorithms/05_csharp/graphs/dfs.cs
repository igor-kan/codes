using System.Collections.Generic;

namespace Algorithms.Graphs
{
    public static class DepthFirstSearch
    {
        public static List<int> Traverse(Dictionary<int, List<int>> graph, int start)
        {
            var visited = new HashSet<int>();
            var stack = new Stack<int>();
            var order = new List<int>();

            stack.Push(start);

            while (stack.Count > 0)
            {
                int node = stack.Pop();
                if (visited.Add(node))
                {
                    order.Add(node);
                    if (graph.TryGetValue(node, out var neighbors))
                    {
                        for (int i = neighbors.Count - 1; i >= 0; i--)
                        {
                            if (!visited.Contains(neighbors[i]))
                            {
                                stack.Push(neighbors[i]);
                            }
                        }
                    }
                }
            }

            return order;
        }
    }
}

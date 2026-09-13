defmodule BFS do
  def bfs(graph, start) do
    bfs_loop(graph, :queue.from_list([start]), MapSet.new([start]), [])
  end
  defp bfs_loop(_, queue, _, acc) when :queue.is_empty(queue), do: Enum.reverse(acc)
  defp bfs_loop(graph, queue, visited, acc) do
    {{:value, node}, rest} = :queue.out(queue)
    neighbors = Map.get(graph, node, [])
    {new_queue, new_visited} = Enum.reduce(neighbors, {rest, visited}, fn n, {q, v} ->
      if MapSet.member?(v, n), do: {q, v}, else: {:queue.in(n, q), MapSet.put(v, n)}
    end)
    bfs_loop(graph, new_queue, new_visited, [node | acc])
  end
end
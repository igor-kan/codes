defmodule InsertionSort do
  def sort(list), do: Enum.reduce(list, [], &insert/2)

  defp insert(x, []), do: [x]
  defp insert(x, [h | t]) when x <= h, do: [x, h | t]
  defp insert(x, [h | t]), do: [h | insert(x, t)]
end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = InsertionSort.sort(data)
unless sorted == Enum.sort(data), do: raise("not sorted")
IO.puts("[Elixir InsertionSort] Insertion sort verified: #{inspect(sorted)}")

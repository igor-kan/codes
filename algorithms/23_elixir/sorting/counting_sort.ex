defmodule CountingSort do
  def sort([]), do: []
  def sort(list) do
    mx = Enum.max(list)
    counts = Enum.frequencies(list)
    Enum.flat_map(0..mx, fn i -> List.duplicate(i, Map.get(counts, i, 0)) end)
  end
end

data = [4, 2, 2, 8, 3, 3, 1]
sorted = CountingSort.sort(data)
unless sorted == Enum.sort(data), do: raise("not sorted")
IO.puts("[Elixir CountingSort] Counting sort verified: #{inspect(sorted)}")

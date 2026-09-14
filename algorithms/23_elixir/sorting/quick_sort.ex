defmodule QuickSort do
  def sort([]), do: []
  def sort([pivot | tail]) do
    {less, greater} = Enum.split_with(tail, &(&1 < pivot))
    sort(less) ++ [pivot] ++ sort(greater)
  end
end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = QuickSort.sort(data)
unless sorted == Enum.sort(data), do: raise("not sorted")
IO.puts("[Elixir QuickSort] Functional quicksort verified: #{inspect(sorted)}")

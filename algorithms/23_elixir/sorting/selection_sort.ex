defmodule SelectionSort do
  def sort([]), do: []
  def sort(list) do
    m = Enum.min(list)
    [m | sort(remove_one(m, list))]
  end

  defp remove_one(_, []), do: []
  defp remove_one(x, [h | t]) when x == h, do: t
  defp remove_one(x, [h | t]), do: [h | remove_one(x, t)]
end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = SelectionSort.sort(data)
unless sorted == Enum.sort(data), do: raise("not sorted")
IO.puts("[Elixir SelectionSort] Selection sort verified: #{inspect(sorted)}")

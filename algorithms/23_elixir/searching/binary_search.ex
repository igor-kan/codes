defmodule BinarySearch do
  def search(arr, target), do: search(arr, target, 0, length(arr) - 1)

  defp search(_arr, _target, lo, hi) when lo > hi, do: -1
  defp search(arr, target, lo, hi) do
    mid = div(lo + hi, 2)
    cond do
      Enum.at(arr, mid) == target -> mid
      Enum.at(arr, mid) < target -> search(arr, target, mid + 1, hi)
      true -> search(arr, target, lo, mid - 1)
    end
  end
end

arr = [1, 3, 5, 7, 9, 11, 13]
unless BinarySearch.search(arr, 7) == 3, do: raise("found wrong")
unless BinarySearch.search(arr, 8) == -1, do: raise("missing wrong")
unless BinarySearch.search(arr, 1) == 0, do: raise("left edge wrong")
IO.puts("[Elixir BinarySearch] Binary search verified")

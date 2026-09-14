defmodule LIS do
  def lis([]), do: 0
  def lis(list) do
    list
    |> Enum.with_index()
    |> Enum.reduce([], fn {x, i}, dp ->
      len =
        Enum.reduce(Enum.with_index(Enum.take(list, i)), 1, fn {y, j}, acc ->
          if y < x, do: max(acc, Enum.at(dp, j) + 1), else: acc
        end)
      dp ++ [len]
    end)
    |> Enum.max()
  end
end

unless LIS.lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4, do: raise("lis wrong")
unless LIS.lis([]) == 0, do: raise("lis empty wrong")
IO.puts("[Elixir LIS] Longest increasing subsequence verified")

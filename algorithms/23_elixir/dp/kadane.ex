defmodule Kadane do
  def max_subarray([h | t]) do
    {_, best} =
      Enum.reduce(t, {h, h}, fn x, {cur, best} ->
        cur2 = max(x, cur + x)
        {cur2, max(best, cur2)}
      end)
    best
  end
end

unless Kadane.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, do: raise("kadane wrong")
unless Kadane.max_subarray([-5, -2, -3]) == -2, do: raise("kadane all-negative wrong")
IO.puts("[Elixir Kadane] Maximum subarray sum verified")

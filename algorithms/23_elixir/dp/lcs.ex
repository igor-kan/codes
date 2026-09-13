defmodule LCS do
  def lcs(a, b) when is_binary(a) and is_binary(b) do
    lcs(String.graphemes(a), String.graphemes(b))
  end
  def lcs([], _), do: 0
  def lcs(_, []), do: 0
  def lcs([h|t1], [h|t2]), do: 1 + lcs(t1, t2)
  def lcs([_|t1]=a, [_|t2]=b), do: max(lcs(a, t2), lcs(t1, b))
end
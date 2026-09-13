defmodule MergeSort do
  def sort([]), do: []
  def sort([x]), do: [x]
  def sort(list) do
    {left, right} = Enum.split(list, div(length(list), 2))
    merge(sort(left), sort(right))
  end
  defp merge([], r), do: r
  defp merge(l, []), do: l
  defp merge([h1|t1], [h2|_]=r) when h1<=h2, do: [h1|merge(t1,r)]
  defp merge(l, [h2|t2]), do: [h2|merge(l,t2)]
end
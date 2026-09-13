defmodule BubbleSort do
  def sort([]), do: []
  def sort(list) do
    {new_list, swapped?} = pass(list)
    if swapped?, do: sort(new_list), else: new_list
  end
  defp pass([a, b | rest]) when a > b, do: {[b | elem(pass([a | rest]), 0)], true}
  defp pass([a | rest]) do
    {sorted, s} = pass(rest)
    {[a | sorted], s}
  end
  defp pass([]), do: {[], false}
end
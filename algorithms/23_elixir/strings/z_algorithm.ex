defmodule ZAlgorithm do
  def z_algorithm(s) do
    chars = String.graphemes(s)
    n = length(chars)
    z = if n > 0, do: [n | List.duplicate(0, n - 1)], else: []
    {z, _} =
      Enum.reduce(1..(n - 1), {z, {0, 0}}, fn i, {z, {l, r}} ->
        zi = if i <= r, do: min(r - i + 1, Enum.at(z, i - l)), else: 0
        zi = extend(chars, i, zi)
        z = List.replace_at(z, i, zi)
        {l, r} = if i + zi - 1 > r, do: {i, i + zi - 1}, else: {l, r}
        {z, {l, r}}
      end)
    z
  end

  defp extend(chars, i, zi) do
    n = length(chars)
    cond do
      i + zi < n and Enum.at(chars, zi) == Enum.at(chars, i + zi) ->
        extend(chars, i, zi + 1)
      true -> zi
    end
  end
end

unless ZAlgorithm.z_algorithm("abacaba") == [7, 0, 1, 0, 3, 0, 1], do: raise("z wrong")
IO.puts("[Elixir ZAlgorithm] Z-algorithm verified")

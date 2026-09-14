defmodule Manacher do
  def longest_palindrome(s) do
    t = "#" <> (s |> String.graphemes() |> Enum.join("#")) <> "#"
    chars = String.graphemes(t)
    n = length(chars)
    {p, _} =
      Enum.reduce(0..(n - 1), {List.duplicate(0, n), {0, 0}}, fn i, {p, {c, r}} ->
        pi = if i < r, do: min(r - i, Enum.at(p, 2 * c - i)), else: 0
        pi = extend(chars, i, pi)
        p = List.replace_at(p, i, pi)
        {c, r} = if i + pi > r, do: {i, i + pi}, else: {c, r}
        {p, {c, r}}
      end)
    Enum.max(p)
  end

  defp extend(chars, i, pi) do
    n = length(chars)
    cond do
      i + pi + 1 < n and i - pi - 1 >= 0 and
          Enum.at(chars, i + pi + 1) == Enum.at(chars, i - pi - 1) ->
        extend(chars, i, pi + 1)
      true -> pi
    end
  end
end

unless Manacher.longest_palindrome("abba") == 4, do: raise("manacher even wrong")
unless Manacher.longest_palindrome("racecar") == 7, do: raise("manacher odd wrong")
IO.puts("[Elixir Manacher] Longest palindromic substring verified")

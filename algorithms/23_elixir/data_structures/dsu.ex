defmodule DSU do
  defstruct parent: [], rank: []

  def new(n), do: %DSU{parent: Enum.to_list(0..(n - 1)), rank: List.duplicate(0, n)}

  def find(%DSU{} = dsu, x) do
    p = Enum.at(dsu.parent, x)
    if p == x do
      {x, dsu}
    else
      {root, dsu2} = find(dsu, p)
      {root, %{dsu2 | parent: List.replace_at(dsu2.parent, x, root)}}
    end
  end

  def union(%DSU{} = dsu, x, y) do
    {rx, dsu1} = find(dsu, x)
    {ry, dsu2} = find(dsu1, y)
    if rx == ry do
      dsu2
    else
      rx_rank = Enum.at(dsu2.rank, rx)
      ry_rank = Enum.at(dsu2.rank, ry)
      cond do
        rx_rank < ry_rank -> %{dsu2 | parent: List.replace_at(dsu2.parent, rx, ry)}
        rx_rank > ry_rank -> %{dsu2 | parent: List.replace_at(dsu2.parent, ry, rx)}
        true ->
          %{dsu2
            | parent: List.replace_at(dsu2.parent, ry, rx),
              rank: List.replace_at(dsu2.rank, rx, rx_rank + 1)}
      end
    end
  end

  def connected(%DSU{} = dsu, x, y) do
    {rx, _} = find(dsu, x)
    {ry, _} = find(dsu, y)
    rx == ry
  end
end

dsu =
  DSU.new(5)
  |> DSU.union(0, 1)
  |> DSU.union(1, 2)
  |> DSU.union(3, 4)

unless DSU.connected(dsu, 0, 2), do: raise("union failed")
if DSU.connected(dsu, 0, 3), do: raise("spurious union")
IO.puts("[Elixir DSU] Disjoint set union verified")

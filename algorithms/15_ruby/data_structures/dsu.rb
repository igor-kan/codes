class DSU
  def initialize(n)
    @parent = (0...n).to_a
    @rank = Array.new(n, 0)
  end

  def find(x)
    @parent[x] = find(@parent[x]) if @parent[x] != x
    @parent[x]
  end

  def union(x, y)
    rx, ry = find(x), find(y)
    return if rx == ry
    if @rank[rx] < @rank[ry]
      @parent[rx] = ry
    elsif @rank[rx] > @rank[ry]
      @parent[ry] = rx
    else
      @parent[ry] = rx
      @rank[rx] += 1
    end
  end

  def connected?(x, y)
    find(x) == find(y)
  end
end

dsu = DSU.new(5)
dsu.union(0, 1)
dsu.union(1, 2)
dsu.union(3, 4)
raise "union failed" unless dsu.connected?(0, 2)
raise "spurious union" if dsu.connected?(0, 3)
puts "[Ruby DSU] Disjoint set union verified"

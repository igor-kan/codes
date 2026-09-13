defmodule MathUtils do
  def gcd(a, 0), do: a
  def gcd(a, b), do: gcd(b, rem(a, b))
  def lcm(a, b), do: div(a, gcd(a, b)) * b
end
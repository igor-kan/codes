object GcdLcm {
  def gcd(a: Long, b: Long): Long = if(b==0) a else gcd(b, a%b)
  def lcm(a: Long, b: Long): Long = a/gcd(a,b)*b
}
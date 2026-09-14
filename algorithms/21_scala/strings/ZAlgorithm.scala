object ZAlgorithm {
  def zAlgorithm(s: String): Array[Int] = {
    val n = s.length
    val z = new Array[Int](n)
    if (n == 0) return z
    z(0) = n
    var l = 0
    var r = 0
    for (i <- 1 until n) {
      if (i <= r) z(i) = math.min(r - i + 1, z(i - l))
      while (i + z(i) < n && s.charAt(z(i)) == s.charAt(i + z(i))) z(i) += 1
      if (i + z(i) - 1 > r) { l = i; r = i + z(i) - 1 }
    }
    z
  }

  def main(args: Array[String]): Unit = {
    assert(zAlgorithm("abacaba").sameElements(Array(7, 0, 1, 0, 3, 0, 1)), "z wrong")
    println("[Scala ZAlgorithm] Z-algorithm verified")
  }
}

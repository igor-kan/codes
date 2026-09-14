object Manacher {
  def manacher(s: String): Int = {
    val t = "#" + s.mkString("#") + "#"
    val n = t.length
    val p = new Array[Int](n)
    var c = 0
    var r = 0
    for (i <- 0 until n) {
      if (i < r) p(i) = math.min(r - i, p(2 * c - i))
      while (i + p(i) + 1 < n && i - p(i) - 1 >= 0 &&
             t.charAt(i + p(i) + 1) == t.charAt(i - p(i) - 1))
        p(i) += 1
      if (i + p(i) > r) { c = i; r = i + p(i) }
    }
    p.max
  }

  def main(args: Array[String]): Unit = {
    assert(manacher("abba") == 4, "manacher even wrong")
    assert(manacher("racecar") == 7, "manacher odd wrong")
    println("[Scala Manacher] Longest palindromic substring verified")
  }
}

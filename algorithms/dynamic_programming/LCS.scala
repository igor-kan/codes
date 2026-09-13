object LongestCommonSubsequence {
  def lcsLength(s1: String, s2: String): Int = {
    val m = s1.length
    val n = s2.length
    val dp = Array.ofDim[Int](m + 1, n + 1)

    for (i <- 1 to m; j <- 1 to n) {
      if (s1(i - 1) == s2(j - 1)) {
        dp(i)(j) = dp(i - 1)(j - 1) + 1
      } else {
        dp(i)(j) = Math.max(dp(i - 1)(j), dp(i)(j - 1))
      }
    }
    dp(m)(n)
  }

  def main(args: Array[String]): Unit = {
    val len = lcsLength("AGGTAB", "GXTXAYB")
    println(s"[Scala LCS] LCS('AGGTAB', 'GXTXAYB') = $len")
    assert(len == 4)
  }
}

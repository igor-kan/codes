object LIS {
  def lis(arr: Array[Int]): Int = {
    if (arr.isEmpty) return 0
    val dp = Array.fill(arr.length)(1)
    for (i <- 1 until arr.length; j <- 0 until i)
      if (arr(j) < arr(i)) dp(i) = math.max(dp(i), dp(j) + 1)
    dp.max
  }

  def main(args: Array[String]): Unit = {
    assert(lis(Array(10, 9, 2, 5, 3, 7, 101, 18)) == 4, "lis wrong")
    assert(lis(Array.emptyIntArray) == 0, "lis empty wrong")
    println("[Scala LIS] Longest increasing subsequence verified")
  }
}

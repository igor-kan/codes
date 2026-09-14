object Kadane {
  def kadane(arr: Array[Int]): Int = {
    var best = arr(0)
    var cur = arr(0)
    for (i <- 1 until arr.length) {
      cur = math.max(arr(i), cur + arr(i))
      best = math.max(best, cur)
    }
    best
  }

  def main(args: Array[String]): Unit = {
    assert(kadane(Array(-2, 1, -3, 4, -1, 2, 1, -5, 4)) == 6, "kadane wrong")
    assert(kadane(Array(-5, -2, -3)) == -2, "kadane all-negative wrong")
    println("[Scala Kadane] Maximum subarray sum verified")
  }
}

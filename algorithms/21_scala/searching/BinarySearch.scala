object BinarySearch {
  def binarySearch(arr: Array[Int], target: Int): Int = {
    var lo = 0
    var hi = arr.length - 1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (arr(mid) == target) return mid
      else if (arr(mid) < target) lo = mid + 1
      else hi = mid - 1
    }
    -1
  }

  def main(args: Array[String]): Unit = {
    val arr = Array(1, 3, 5, 7, 9, 11, 13)
    assert(binarySearch(arr, 7) == 3, "found index wrong")
    assert(binarySearch(arr, 8) == -1, "missing target wrong")
    assert(binarySearch(arr, 1) == 0, "left edge wrong")
    println("[Scala BinarySearch] Binary search verified")
  }
}

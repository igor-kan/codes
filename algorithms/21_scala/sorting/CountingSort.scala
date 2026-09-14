object CountingSort {
  def countingSort(arr: Array[Int]): Array[Int] = {
    if (arr.isEmpty) return Array.emptyIntArray
    val maxVal = arr.max
    val count = Array.fill(maxVal + 1)(0)
    arr.foreach(x => count(x) += 1)
    for (i <- 1 to maxVal) count(i) += count(i - 1)
    val out = new Array[Int](arr.length)
    arr.reverse.foreach { x =>
      count(x) -= 1
      out(count(x)) = x
    }
    out
  }

  def main(args: Array[String]): Unit = {
    val data = Array(4, 2, 2, 8, 3, 3, 1)
    val sorted = countingSort(data)
    assert(sorted.sameElements(data.sorted), "not sorted")
    println(s"[Scala CountingSort] Counting sort verified: ${sorted.mkString(", ")}")
  }
}

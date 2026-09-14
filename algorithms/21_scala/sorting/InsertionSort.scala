object InsertionSort {
  def insertionSort(arr: Array[Int]): Array[Int] = {
    val a = arr.clone()
    for (i <- 1 until a.length) {
      val key = a(i)
      var j = i - 1
      while (j >= 0 && a(j) > key) {
        a(j + 1) = a(j)
        j -= 1
      }
      a(j + 1) = key
    }
    a
  }

  def main(args: Array[String]): Unit = {
    val data = Array(33, 7, 91, 12, 5, 5, 78, 2, 44, 19)
    val sorted = insertionSort(data)
    assert(sorted.sameElements(data.sorted), "not sorted")
    println(s"[Scala InsertionSort] Insertion sort verified: ${sorted.mkString(", ")}")
  }
}

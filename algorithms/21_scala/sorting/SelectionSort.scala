object SelectionSort {
  def selectionSort(arr: Array[Int]): Array[Int] = {
    val a = arr.clone()
    for (i <- 0 until a.length - 1) {
      var minIdx = i
      for (j <- i + 1 until a.length) if (a(j) < a(minIdx)) minIdx = j
      val tmp = a(i); a(i) = a(minIdx); a(minIdx) = tmp
    }
    a
  }

  def main(args: Array[String]): Unit = {
    val data = Array(33, 7, 91, 12, 5, 5, 78, 2, 44, 19)
    val sorted = selectionSort(data)
    assert(sorted.sameElements(data.sorted), "not sorted")
    println(s"[Scala SelectionSort] Selection sort verified: ${sorted.mkString(", ")}")
  }
}

object QuickSort {
  def sort[T](arr: List[T])(implicit ord: Ordering[T]): List[T] = arr match {
    case Nil => Nil
    case pivot :: tail =>
      val (less, greater) = tail.partition(ord.lt(_, pivot))
      sort(less) ::: pivot :: sort(greater)
  }

  def main(args: Array[String]): Unit = {
    val data = List(33, 7, 91, 12, 5, 5, 78, 2, 44, 19)
    val sorted = sort(data)
    assert(sorted == data.sorted, "not sorted")
    println(s"[Scala QuickSort] Functional quicksort verified: $sorted")
  }
}

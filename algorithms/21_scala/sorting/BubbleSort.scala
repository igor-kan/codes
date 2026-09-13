object BubbleSort {
  def sort[T: Ordering](arr: Array[T]): Array[T] = {
    val a = arr.clone(); val ord = implicitly[Ordering[T]]
    for (i <- a.indices; j <- 0 until a.length-i-1)
      if (ord.gt(a(j), a(j+1))) { val t=a(j); a(j)=a(j+1); a(j+1)=t }
    a
  }
}
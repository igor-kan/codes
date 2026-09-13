object MergeSort {
  def sort[T: Ordering](arr: List[T]): List[T] = arr match {
    case Nil | List(_) => arr
    case _ =>
      val (l,r) = arr.splitAt(arr.size/2)
      merge(sort(l), sort(r))
  }
  def merge[T](l:List[T],r:List[T])(implicit ord:Ordering[T]):List[T]=(l,r) match {
    case (Nil,_) => r; case (_,Nil) => l
    case (x::xs,y::ys) => if(ord.lteq(x,y)) x::merge(xs,r) else y::merge(l,ys)
  }
}
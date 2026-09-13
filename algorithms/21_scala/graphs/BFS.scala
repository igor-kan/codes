import scala.collection.mutable
object BFS {
  def bfs(graph: Map[Int,List[Int]], start: Int): List[Int] = {
    val visited = mutable.Set[Int](); val queue = mutable.Queue(start); val order = mutable.ListBuffer[Int]()
    while (queue.nonEmpty) { val u=queue.dequeue()
      if (!visited(u)) { visited+=u; order+=u; queue++=graph.getOrElse(u,Nil) } }
    order.toList
  }
}
module graph_mod
  implicit none
contains
  function bfs(adj, n, start, order, order_size) result(ok)
    integer, intent(in) :: n, start
    integer, intent(in) :: adj(n, 0:n)
    integer, intent(out) :: order(n)
    integer, intent(out) :: order_size
    logical :: ok
    logical :: visited(n)
    integer :: queue(n)
    integer :: q_front, q_back, u, v, i, deg
    ok = .true.
    visited = .false.
    q_front = 1
    q_back = 1
    order_size = 0
    visited(start) = .true.
    queue(q_back) = start
    q_back = q_back + 1
    do while (q_front < q_back)
      u = queue(q_front)
      q_front = q_front + 1
      order_size = order_size + 1
      order(order_size) = u
      deg = adj(u, 0)
      do i = 1, deg
        v = adj(u, i)
        if (.not. visited(v)) then
          visited(v) = .true.
          queue(q_back) = v
          q_back = q_back + 1
        end if
      end do
    end do
  end function bfs
end module graph_mod

program test_bfs
  use graph_mod
  implicit none
  integer, parameter :: n = 6
  integer :: adj(n, 0:n)
  integer :: order(n), order_size, i
  logical :: ok

  adj = 0
  adj(1, 0) = 2; adj(1, 1) = 2; adj(1, 2) = 3
  adj(2, 0) = 2; adj(2, 1) = 1; adj(2, 2) = 4
  adj(3, 0) = 2; adj(3, 1) = 1; adj(3, 2) = 5
  adj(4, 0) = 1; adj(4, 1) = 2
  adj(5, 0) = 1; adj(5, 1) = 3
  adj(6, 0) = 0

  print *, "[Fortran BFS] Testing BFS on adjacency list"
  ok = bfs(adj, n, 1, order, order_size)
  print *, "Order size:", order_size
  print *, "BFS order:", (order(i), i=1, order_size)
  print *, "[Fortran BFS] Test completed."
end program test_bfs
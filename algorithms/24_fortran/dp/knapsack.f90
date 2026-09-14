module dp_mod
  implicit none
contains
  function knapsack(weights, values, n, capacity) result(max_val)
    integer, intent(in) :: n, capacity
    integer, intent(in) :: weights(n), values(n)
    integer :: max_val
    integer :: dp(0:n, 0:capacity)
    integer :: i, w
    dp = 0
    do i = 1, n
      do w = 0, capacity
        if (weights(i) > w) then
          dp(i, w) = dp(i - 1, w)
        else
          dp(i, w) = max(dp(i - 1, w), dp(i - 1, w - weights(i)) + values(i))
        end if
      end do
    end do
    max_val = dp(n, capacity)
  end function knapsack
end module dp_mod

program test_knapsack
  use dp_mod
  implicit none
  integer, parameter :: n = 4
  integer :: weights(n) = (/2, 3, 4, 5/)
  integer :: values(n) = (/3, 4, 5, 6/)
  integer :: capacity = 8
  integer :: result
  print *, "[Fortran Knapsack] Testing 0/1 knapsack"
  result = knapsack(weights, values, n, capacity)
  print *, "Weights: ", weights
  print *, "Values:  ", values
  print *, "Capacity:", capacity
  print *, "Maximum value:", result
  print *, "Expected: 10"
  print *, "[Fortran Knapsack] Test completed."
end program test_knapsack
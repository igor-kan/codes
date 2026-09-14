module quick_sort_mod
  implicit none
contains
  recursive subroutine quick_sort(arr, lo, hi)
    integer, intent(inout) :: arr(:)
    integer, intent(in) :: lo, hi
    integer :: p
    if (lo < hi) then
      p = partition(arr, lo, hi)
      call quick_sort(arr, lo, p - 1)
      call quick_sort(arr, p + 1, hi)
    end if
  end subroutine quick_sort

  integer function partition(arr, lo, hi) result(p)
    integer, intent(inout) :: arr(:)
    integer, intent(in) :: lo, hi
    integer :: pivot, i, j, tmp
    pivot = arr(hi)
    i = lo - 1
    do j = lo, hi - 1
      if (arr(j) <= pivot) then
        i = i + 1
        tmp = arr(i); arr(i) = arr(j); arr(j) = tmp
      end if
    end do
    tmp = arr(i + 1); arr(i + 1) = arr(hi); arr(hi) = tmp
    p = i + 1
  end function partition
end module quick_sort_mod

program test_quick_sort
  use quick_sort_mod
  implicit none
  integer, parameter :: n = 10
  integer :: data(n), i
  logical :: ok

  data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
  call quick_sort(data, 1, n)

  ok = .true.
  do i = 2, n
    if (data(i - 1) > data(i)) ok = .false.
  end do

  print *, "[Fortran QuickSort] Testing recursive quicksort"
  if (ok) then
    print *, "Sorted:", data
    print *, "[Fortran QuickSort] Recursive quicksort verified."
  else
    print *, "FAILED: array not sorted"
  end if
end program test_quick_sort

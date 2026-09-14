module merge_sort_mod
  implicit none
contains
  recursive subroutine merge_sort(arr, lo, hi)
    integer, intent(inout) :: arr(:)
    integer, intent(in) :: lo, hi
    integer :: mid
    if (lo < hi) then
      mid = lo + (hi - lo) / 2
      call merge_sort(arr, lo, mid)
      call merge_sort(arr, mid + 1, hi)
      call merge_halves(arr, lo, mid, hi)
    end if
  end subroutine merge_sort

  subroutine merge_halves(arr, lo, mid, hi)
    integer, intent(inout) :: arr(:)
    integer, intent(in) :: lo, mid, hi
    integer, allocatable :: tmp(:)
    integer :: i, j, k
    allocate(tmp(hi - lo + 1))
    i = lo; j = mid + 1; k = 1
    do while (i <= mid .and. j <= hi)
      if (arr(i) <= arr(j)) then
        tmp(k) = arr(i); i = i + 1
      else
        tmp(k) = arr(j); j = j + 1
      end if
      k = k + 1
    end do
    do while (i <= mid)
      tmp(k) = arr(i); i = i + 1; k = k + 1
    end do
    do while (j <= hi)
      tmp(k) = arr(j); j = j + 1; k = k + 1
    end do
    arr(lo:hi) = tmp
    deallocate(tmp)
  end subroutine merge_halves
end module merge_sort_mod

program test_merge_sort
  use merge_sort_mod
  implicit none
  integer, parameter :: n = 10
  integer :: data(n), i
  logical :: ok

  data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
  call merge_sort(data, 1, n)

  ok = .true.
  do i = 2, n
    if (data(i - 1) > data(i)) ok = .false.
  end do

  print *, "[Fortran MergeSort] Testing recursive merge sort"
  if (ok) then
    print *, "Sorted:", data
    print *, "[Fortran MergeSort] Recursive merge sort verified."
  else
    print *, "FAILED: array not sorted"
  end if
end program test_merge_sort

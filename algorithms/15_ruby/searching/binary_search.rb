def binary_search(arr, target)
  lo, hi = 0, arr.length - 1
  while lo <= hi
    mid = (lo + hi) / 2
    if arr[mid] == target
      return mid
    elsif arr[mid] < target
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  -1
end

arr = [1, 3, 5, 7, 9, 11, 13]
raise "found index wrong" unless binary_search(arr, 7) == 3
raise "missing target wrong" unless binary_search(arr, 8) == -1
raise "edge left wrong" unless binary_search(arr, 1) == 0
puts "[Ruby BinarySearch] Binary search verified"

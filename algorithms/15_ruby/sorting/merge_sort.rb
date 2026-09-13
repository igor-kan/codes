def merge_sort(arr)
  return arr if arr.length <= 1
  m = arr.length / 2
  merge(merge_sort(arr[0...m]), merge_sort(arr[m..]))
end
def merge(l, r)
  res = []; i = j = 0
  while i < l.length && j < r.length
    res << (l[i] <= r[j] ? l[i += 1; i-1] : r[j += 1; j-1])
  end
  res + l[i..] + r[j..]
end
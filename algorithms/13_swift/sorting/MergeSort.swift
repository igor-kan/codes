func mergeSort<T: Comparable>(_ arr: [T]) -> [T] {
    guard arr.count > 1 else { return arr }
    let m = arr.count/2
    return merge(mergeSort(Array(arr[..<m])), mergeSort(Array(arr[m...])))
}
func merge<T: Comparable>(_ l: [T], _ r: [T]) -> [T] {
    var res=[T](); var i=0,j=0
    while i<l.count&&j<r.count { if l[i]<=r[j]{res.append(l[i]);i+=1}else{res.append(r[j]);j+=1} }
    return res+l[i...]+r[j...]
}
fun <T : Comparable<T>> mergeSort(arr: List<T>): List<T> {
    if (arr.size <= 1) return arr
    val m = arr.size / 2
    return merge(mergeSort(arr.subList(0,m)), mergeSort(arr.subList(m,arr.size)))
}
fun <T : Comparable<T>> merge(l: List<T>, r: List<T>): List<T> {
    val res = mutableListOf<T>(); var i=0; var j=0
    while (i<l.size&&j<r.size) if(l[i]<=r[j]) res+=l[i++] else res+=r[j++]
    return res+l.subList(i,l.size)+r.subList(j,r.size)
}
fun <T : Comparable<T>> bubbleSort(arr: MutableList<T>): List<T> {
    val a = arr.toMutableList()
    for (i in a.indices) for (j in 0 until a.size-i-1) if (a[j] > a[j+1]) { val t=a[j]; a[j]=a[j+1]; a[j+1]=t }
    return a
}
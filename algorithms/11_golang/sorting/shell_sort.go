package sorting
func ShellSort(arr []int) {
    n := len(arr)
    h := 1
    for h < n/3 { h = 3*h + 1 }
    for h >= 1 {
        for i := h; i < n; i++ {
            temp := arr[i]
            j := i
            for j >= h && arr[j-h] > temp {
                arr[j] = arr[j-h]
                j -= h
            }
            arr[j] = temp
        }
        h /= 3
    }
}

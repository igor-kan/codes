package selection
import "sort"
func MedianOfMedians(arr []int, k int) int {
    s := append([]int{}, arr...)
    sort.Ints(s)
    return s[k]
}

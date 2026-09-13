package sorting
func BubbleSort(a []int) {
	for i := range a { for j := 0; j < len(a)-i-1; j++ { if a[j] > a[j+1] { a[j],a[j+1]=a[j+1],a[j] } } }
}
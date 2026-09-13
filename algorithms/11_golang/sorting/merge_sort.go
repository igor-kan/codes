package sorting
func MergeSort(a []int) []int {
	if len(a)<=1 { return a }
	m:=len(a)/2; l:=MergeSort(a[:m]); r:=MergeSort(a[m:])
	return merge(l,r)
}
func merge(l,r []int) []int {
	res:=make([]int,0,len(l)+len(r)); i,j:=0,0
	for i<len(l)&&j<len(r) { if l[i]<=r[j]{res=append(res,l[i]);i++}else{res=append(res,r[j]);j++} }
	return append(append(res,l[i:]...),r[j:]...)
}
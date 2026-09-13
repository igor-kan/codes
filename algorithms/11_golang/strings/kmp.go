package strings
func KMP(text,pat string) []int {
	lps:=makeLPS(pat); matches:=[]int{}; j:=0
	for i:=0;i<len(text);{
		if text[i]==pat[j] { i++;j++ }
		if j==len(pat) { matches=append(matches,i-j); j=lps[j-1] } else if i<len(text)&&text[i]!=pat[j] {
			if j!=0 { j=lps[j-1] } else { i++ } } }
	return matches
}
func makeLPS(p string) []int {
	lps:=make([]int,len(p)); k:=0
	for i:=1;i<len(p);{ if p[i]==p[k] { lps[i]=k+1;i++;k++ } else if k!=0 { k=lps[k-1] } else { i++ } }
	return lps
}
package math
func Sieve(n int) []int {
	is:=make([]bool,n+1); for i:=range is { is[i]=true }; is[0]=false; is[1]=false
	for i:=2;i*i<=n;i++ { if is[i] { for j:=i*i;j<=n;j+=i { is[j]=false } } }
	primes:=[]int{}; for i,v:=range is { if v { primes=append(primes,i) } }; return primes
}
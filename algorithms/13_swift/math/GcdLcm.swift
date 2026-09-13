func gcd(_ a: Int,_ b: Int)->Int{ b==0 ? a : gcd(b,a%b) }
func lcm(_ a: Int,_ b: Int)->Int{ a/gcd(a,b)*b }
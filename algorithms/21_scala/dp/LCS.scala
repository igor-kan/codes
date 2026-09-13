object LCS {
  def lcs(a: String, b: String): Int = {
    val (m,n)=(a.length,b.length)
    val dp=Array.ofDim[Int](m+1,n+1)
    for(i<-1 to m; j<-1 to n)
      dp(i)(j)=if(a(i-1)==b(j-1)) dp(i-1)(j-1)+1 else dp(i-1)(j).max(dp(i)(j-1))
    dp(m)(n)
  }
}
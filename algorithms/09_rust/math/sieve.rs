pub fn sieve(n:usize)->Vec<usize>{
    let mut is=vec![true;n+1]; is[0]=false; if n>0{is[1]=false;}
    let mut i=2; while i*i<=n{ if is[i]{ let mut j=i*i; while j<=n{is[j]=false;j+=i;} } i+=1; }
    (0..=n).filter(|&i|is[i]).collect()
}
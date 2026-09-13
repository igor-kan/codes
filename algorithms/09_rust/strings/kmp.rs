pub fn kmp(text:&[u8],pat:&[u8])->Vec<usize>{
    let lps=make_lps(pat); let mut matches=vec![]; let mut j=0;
    for (i,&c) in text.iter().enumerate(){
        while j>0&&c!=pat[j]{ j=lps[j-1]; }
        if c==pat[j]{ j+=1; }
        if j==pat.len(){ matches.push(i+1-j); j=lps[j-1]; } }
    matches
}
fn make_lps(p:&[u8])->Vec<usize>{
    let mut lps=vec![0usize;p.len()]; let mut k=0;
    for i in 1..p.len(){
        while k>0&&p[i]!=p[k]{ k=lps[k-1]; }
        if p[i]==p[k]{ k+=1; } lps[i]=k; }
    lps
}
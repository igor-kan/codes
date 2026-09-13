pub fn merge_sort(a: &[i64]) -> Vec<i64> {
    if a.len()<=1 { return a.to_vec(); }
    let m=a.len()/2; let (l,r)=(merge_sort(&a[..m]),merge_sort(&a[m..]));
    let (mut i,mut j,mut res)=(0,0,vec![]);
    while i<l.len()&&j<r.len() { if l[i]<=r[j]{res.push(l[i]);i++;}else{res.push(r[j]);j++;} }
    res.extend_from_slice(&l[i..]); res.extend_from_slice(&r[j..]); res
}
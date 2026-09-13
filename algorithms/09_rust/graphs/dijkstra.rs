use std::collections::{BinaryHeap,HashMap}; use std::cmp::Reverse;
pub fn dijkstra(graph:&HashMap<i32,Vec<(i32,i64)>>,src:i32)->HashMap<i32,i64>{
    let mut dist=HashMap::from([(src,0i64)]); let mut heap=BinaryHeap::from([Reverse((0i64,src))]);
    while let Some(Reverse((d,u)))=heap.pop(){
        if d>*dist.get(&u).unwrap_or(&i64::MAX){ continue; }
        for &(v,w) in graph.get(&u).unwrap_or(&vec![]){
            let nd=d+w; if nd<*dist.get(&v).unwrap_or(&i64::MAX){ dist.insert(v,nd); heap.push(Reverse((nd,v))); } } }
    dist
}
use std::collections::{HashMap,HashSet,VecDeque};
pub fn bfs(graph:&HashMap<i32,Vec<i32>>,start:i32)->Vec<i32>{
    let mut visited=HashSet::new(); let mut q=VecDeque::from([start]); let mut order=vec![];
    while let Some(node)=q.pop_front(){
        if visited.insert(node){ order.push(node);
            if let Some(nb)=graph.get(&node){ for &v in nb { q.push_back(v); } } } }
    order
}
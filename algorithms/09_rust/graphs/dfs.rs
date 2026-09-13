use std::collections::{HashMap,HashSet};
pub fn dfs(graph:&HashMap<i32,Vec<i32>>,start:i32)->Vec<i32>{
    let mut visited=HashSet::new(); let mut stack=vec![start]; let mut order=vec![];
    while let Some(node)=stack.pop(){
        if visited.insert(node){ order.push(node);
            if let Some(nb)=graph.get(&node){ for &v in nb.iter().rev(){ stack.push(v); } } } }
    order
}
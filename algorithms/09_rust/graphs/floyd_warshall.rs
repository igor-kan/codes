//! All-pairs shortest paths (Floyd-Warshall).
const INF: i64 = i64::MAX / 4;

fn floyd_warshall(mut dist: Vec<Vec<i64>>) -> Vec<Vec<i64>> {
    let n = dist.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                let through = dist[i][k].saturating_add(dist[k][j]);
                if through < dist[i][j] {
                    dist[i][j] = through;
                }
            }
        }
    }
    dist
}

fn main() {
    let graph = vec![
        vec![0, 3, INF, 7],
        vec![8, 0, 2, INF],
        vec![5, INF, 0, 1],
        vec![2, INF, INF, 0],
    ];
    let dist = floyd_warshall(graph);
    assert_eq!(dist[0][2], 5);
    assert_eq!(dist[0][3], 6);
    println!("{:?}", dist[0]);
}

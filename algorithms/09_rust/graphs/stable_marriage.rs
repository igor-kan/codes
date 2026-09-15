//! Gale-Shapley stable matching.
fn main() {
    let men_prefs = [[0usize, 1, 2], [1, 0, 2], [0, 1, 2]];
    let women_prefs = [[2usize, 1, 0], [0, 1, 2], [0, 1, 2]];
    let n = 3;
    let mut rank = [[0usize; 3]; 3];
    for w in 0..n {
        for (i, &m) in women_prefs[w].iter().enumerate() {
            rank[w][m] = i;
        }
    }
    let mut free: Vec<usize> = (0..n).collect();
    let mut next = [0usize; 3];
    let mut engaged_to = [-1isize; 3];
    while let Some(m) = free.pop() {
        let w = men_prefs[m][next[m]];
        next[m] += 1;
        if engaged_to[w] == -1 {
            engaged_to[w] = m as isize;
        } else {
            let current = engaged_to[w] as usize;
            if rank[w][m] < rank[w][current] {
                free.push(current);
                engaged_to[w] = m as isize;
            } else {
                free.push(m);
            }
        }
    }
    assert_eq!(engaged_to, [2, 0, 1]);
    println!("stable marriage ok");
}

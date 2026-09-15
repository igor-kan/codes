fn team(problems: &[[i32; 3]]) -> usize {
    problems.iter().filter(|p| p[0] + p[1] + p[2] >= 2).count()
}

fn main() {
    assert_eq!(team(&[[1, 1, 0], [1, 1, 1], [1, 0, 0]]), 2);
    println!("231A team ok");
}

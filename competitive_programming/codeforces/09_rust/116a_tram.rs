fn tram(stops: &[(i32, i32)]) -> i32 {
    let mut current = 0;
    let mut capacity = 0;
    for &(leaving, entering) in stops {
        current += entering - leaving;
        capacity = capacity.max(current);
    }
    capacity
}

fn main() {
    assert_eq!(tram(&[(0, 3), (2, 5), (4, 2), (4, 0)]), 6);
    println!("116A tram ok");
}

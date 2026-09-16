fn sqrt_x(x: i32) -> i32 {
    let (mut low, mut high) = (0i64, x as i64);
    while low <= high {
        let middle = (low + high) / 2;
        if middle * middle <= x as i64 { low = middle + 1; } else { high = middle - 1; }
    }
    high as i32
}

fn main() {
    assert_eq!(sqrt_x(4), 2);
    assert_eq!(sqrt_x(8), 2);
    assert_eq!(sqrt_x(0), 0);
    println!("69 sqrt x ok");
}

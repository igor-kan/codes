fn wrong_subtraction(number: i64, steps: i32) -> i64 {
    let mut current = number;
    for _ in 0..steps {
        if current % 10 == 0 {
            current /= 10;
        } else {
            current -= 1;
        }
    }
    current
}

fn main() {
    assert_eq!(wrong_subtraction(512, 4), 50);
    assert_eq!(wrong_subtraction(1000000000, 9), 1);
    println!("977A wrong subtraction ok");
}

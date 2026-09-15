fn soldier_and_bananas(cost: i64, money: i64, count: i64) -> i64 {
    let total = cost * count * (count + 1) / 2;
    (total - money).max(0)
}

fn main() {
    assert_eq!(soldier_and_bananas(3, 17, 4), 13);
    assert_eq!(soldier_and_bananas(1, 100, 1), 0);
    println!("546A soldier and bananas ok");
}

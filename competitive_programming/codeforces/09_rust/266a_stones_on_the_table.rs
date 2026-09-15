fn stones_on_table(row: &str) -> i32 {
    let bytes = row.as_bytes();
    (1..bytes.len()).filter(|&i| bytes[i] == bytes[i - 1]).count() as i32
}

fn main() {
    assert_eq!(stones_on_table("RRG"), 1);
    assert_eq!(stones_on_table("RRRRR"), 4);
    assert_eq!(stones_on_table("BRBG"), 0);
    println!("266A stones on the table ok");
}

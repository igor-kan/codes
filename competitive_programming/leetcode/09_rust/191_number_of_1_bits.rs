fn number_of_1_bits(n: u32) -> u32 {
    n.count_ones()
}

fn main() {
    assert_eq!(number_of_1_bits(11), 3);
    assert_eq!(number_of_1_bits(128), 1);
    assert_eq!(number_of_1_bits(4294967293), 31);
    println!("191 number of 1 bits ok");
}

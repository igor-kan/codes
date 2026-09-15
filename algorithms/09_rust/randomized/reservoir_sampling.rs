//! Reservoir sampling for a uniform sample of a stream (CLRS 5.3).
struct Lcg(u64);

impl Lcg {
    fn next(&mut self) -> u64 {
        self.0 = self.0.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        self.0 >> 33
    }
}

fn reservoir_sample(stream: impl Iterator<Item = i32>, k: usize) -> Vec<i32> {
    let mut rng = Lcg(42);
    let mut reservoir: Vec<i32> = Vec::new();
    for (i, item) in stream.enumerate() {
        if i < k {
            reservoir.push(item);
        } else {
            let j = (rng.next() as usize) % (i + 1);
            if j < k {
                reservoir[j] = item;
            }
        }
    }
    reservoir
}

fn main() {
    let sample = reservoir_sample(0..100, 5);
    assert_eq!(sample.len(), 5);
    println!("reservoir sampling ok");
}

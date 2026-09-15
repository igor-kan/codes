//! Fixed-size circular buffer.
struct CircularBuffer {
    data: Vec<i32>,
    head: usize,
    size: usize,
}

impl CircularBuffer {
    fn new(capacity: usize) -> Self {
        CircularBuffer { data: vec![0; capacity], head: 0, size: 0 }
    }
    fn push(&mut self, value: i32) {
        let n = self.data.len();
        self.data[(self.head + self.size) % n] = value;
        if self.size < n {
            self.size += 1;
        } else {
            self.head = (self.head + 1) % n;
        }
    }
    fn pop(&mut self) -> i32 {
        let value = self.data[self.head];
        self.head = (self.head + 1) % self.data.len();
        self.size -= 1;
        value
    }
}

fn main() {
    let mut buffer = CircularBuffer::new(3);
    for i in 1..=4 {
        buffer.push(i);
    }
    assert_eq!(buffer.pop(), 2);
    assert_eq!(buffer.pop(), 3);
    assert_eq!(buffer.pop(), 4);
    println!("circular buffer ok");
}

// Fixed-size circular buffer.
class CircularBuffer {
  constructor(capacity) {
    this.data = new Array(capacity).fill(0);
    this.head = 0;
    this.size = 0;
  }
  get length() {
    return this.size;
  }
  push(value) {
    const n = this.data.length;
    this.data[(this.head + this.size) % n] = value;
    if (this.size < n) {
      this.size += 1;
    } else {
      this.head = (this.head + 1) % n;
    }
  }
  pop() {
    const value = this.data[this.head];
    this.head = (this.head + 1) % this.data.length;
    this.size -= 1;
    return value;
  }
}

const buffer = new CircularBuffer(3);
for (let i = 1; i <= 4; i += 1) buffer.push(i);
if (buffer.pop() !== 2 || buffer.pop() !== 3 || buffer.pop() !== 4) {
  throw new Error("bad overwrite semantics");
}
console.log("circular buffer ok");
